import torch as t
from jukebox.hparams import Hyperparams, setup_hparams
from jukebox.make_models import make_vqvae, make_prior, MODELS
from jukebox.sample import _sample, \
    upsample, \
    load_prompts
from jukebox.utils.dist_utils import setup_dist_from_mpi
from jukebox.utils.torch_utils import empty_cache


def generate(args):
    rank, local_rank, device = setup_dist_from_mpi()
    music_genre = args.music_genre
    artist = args.artist

    model = '5b_lyrics'  # можно поставить 1b
    hps = Hyperparams()
    hps.sr = 44100
    hps.n_samples = 3
    # Сюда будут сохраняться мелодии
    hps.name = args.save_path
    chunk_size = 16 if model in ('5b', '5b_lyrics') else 32
    max_batch_size = 2 if model in ('5b', '5b_lyrics') else 16
    hps.levels = 3
    hps.hop_fraction = [1, 1, .125]

    vqvae, *priors = MODELS[model]
    vqvae = make_vqvae(setup_hparams(vqvae, dict(sample_length=1048576)), device)
    top_prior = make_prior(setup_hparams(priors[-1], dict()), vqvae, device)

    mode = 'ancestral'
    codes_file = None
    audio_file = None
    prompt_length_in_seconds = None

    sample_hps = Hyperparams(
        dict(mode=mode, codes_file=codes_file, audio_file=audio_file,
             prompt_length_in_seconds=prompt_length_in_seconds))

    sample_length_in_seconds = args.sample_len  # Длина мелодии в секундах
    hps.sample_length = (int(sample_length_in_seconds * hps.sr) // top_prior.raw_to_tokens) * top_prior.raw_to_tokens
    assert hps.sample_length >= top_prior.n_ctx * top_prior.raw_to_tokens, f'Please choose a larger sampling rate'

    metas = [dict(artist=artist,  # Музыкант
                  genre=music_genre,  # Жанр
                  total_length=hps.sample_length,
                  offset=0,
                  lyrics="""""",
                  ),
             ] * hps.n_samples
    labels = [None, None, top_prior.labeller.get_batch_labels(metas, 'cuda')]

    sampling_temperature = .98

    lower_batch_size = 16
    max_batch_size = 3 if model in ('5b', '5b_lyrics') else 16
    lower_level_chunk_size = 32
    chunk_size = 16 if model in ('5b', '5b_lyrics') else 32
    sampling_kwargs = [dict(temp=.99, fp16=True, max_batch_size=lower_batch_size,
                            chunk_size=lower_level_chunk_size),
                       dict(temp=0.99, fp16=True, max_batch_size=lower_batch_size,
                            chunk_size=lower_level_chunk_size),
                       dict(temp=sampling_temperature, fp16=True,
                            max_batch_size=max_batch_size, chunk_size=chunk_size)]

    if sample_hps.mode == 'ancestral':
        zs = [t.zeros(hps.n_samples, 0, dtype=t.long, device='cuda') for _ in range(len(priors))]
        zs = _sample(zs, labels, sampling_kwargs, [None, None, top_prior], [2], hps)
    elif sample_hps.mode == 'upsample':
        assert sample_hps.codes_file is not None
        # Load codes.
        data = t.load(sample_hps.codes_file, map_location='cuda')
        zs = [z.cpu() for z in data['zs']]
        assert zs[-1].shape[0] == hps.n_samples, f"Expected bs = {hps.n_samples}, got {zs[-1].shape[0]}"
        del data
        print('Falling through to the upsample step later in the notebook.')
    elif sample_hps.mode == 'primed':
        assert sample_hps.audio_file is not None
        audio_files = sample_hps.audio_file.split(',')
        duration = (
                               int(sample_hps.prompt_length_in_seconds * hps.sr) // top_prior.raw_to_tokens) * top_prior.raw_to_tokens
        x = load_prompts(audio_files, duration, hps)
        zs = top_prior.encode(x, start_level=0, end_level=len(priors), bs_chunks=x.shape[0])
        zs = _sample(zs, labels, sampling_kwargs, [None, None, top_prior], [2], hps)
    else:
        raise ValueError(f'Unknown sample mode {sample_hps.mode}.')

    if True:
        del top_prior
        empty_cache()
        top_prior = None
    upsamplers = [make_prior(setup_hparams(prior, dict()), vqvae, 'cuda') for prior in priors[:-1]]
    labels[:2] = [prior.labeller.get_batch_labels(metas, 'cuda') for prior in upsamplers]

    zs = upsample(zs, labels, sampling_kwargs, [*upsamplers, top_prior], hps)

    del upsamplers
    empty_cache()
