# VideoStories generation

# Part 0

### Preparation
After you add CUDA binaries to `PATH` and `LD_LIBRARY_PATH` you can install this project:
```bash
git clone git@github.com:mrapplexz/aiijc-creative-imagegen.git
cd aiijc-creative-imagegen
./install.sh
```

# Part 1

### Text generation

If your host doesn't provide access to huggingface hub, download 
`pytorch_model.bin`,`tokenizer_config.json`,`vocab.json`,`config.json`,`special_tokens_map.json`, `merges.txt` [here](https://huggingface.co/EleutherAI/gpt-neo-2.7B) 
and start with  `--local_model MODEL_PATH`
```bash
python3_text generate_text.py --device cuda:0                             \
                              --output_filename ./output/texts/text.txt   \
                              --temperature 0.1                           \
                              --top_k 10000                               \
                              --top_p 0.95                                \
                              --repetition_penalty 5.0                    \
                              --max_length 1000                           \
                              --seed 42                                   \
                              --start "The kingdom and a princess"        \
                              --genre fairy_tale
```
# Part 2

Аll the sub-parts of the part 2 can be executed in any order or in parallel

## Part 2.1

### TTS generation

Before start you need to download pretrained model `LibriTTS_800000.tar`
[here](https://drive.google.com/drive/folders/1DOhZGlTLMbbAAFZmZGDdc77kz1PloS7F)
and put it to `./tts_generation/FastSpeech2/output/ckpt/LibriTTS/800000.pth.tar`

If your host doesn't provide access to nltk hub, you need to install `cmudict` and `averaged_perceptron_tagger` packages manually with [this instruction](http://www.nltk.org/data.html) 
```bash
python3_tts generate_tts.py --input_filename ./output/texts/text.txt       \
                            --temp_dir ./tmp                               \
                            --speaker_id 205                               \
                            --output_dir ./output/tts                      
```

## Part 2.2

### Image generation

If your host doesn't provide access to OpenAI hub, you need to download [RN50.pt](https://openaipublic.azureedge.net/clip/models/afeb0e10f9e5a86da6080e35cf09123aca3b358a0c3e3b6c78a7b63bc04b6762/RN50.pt) , [ViT-B-16.pt](https://openaipublic.azureedge.net/clip/models/5806e77cd80f8b59890b7e101eabd078d9fb84e6937f9e85e4ecb61988df416f/ViT-B-16.pt) , [ViT-B-32.pt](https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt) and put them to `~/.cache/clip` 

```bash
python3_image generate_images.py --input_filename ./output/texts/text.txt       \
                                 --devices cuda:0,cuda:1                        \
                                 --main_dir ./output/frames                     
```

## Part 2.3

### Music generation

If your host doesn't provide access to OpenAI hub, you need to download [vqvae.pth.tar](https://openaipublic.azureedge.net/jukebox/models/5b/vqvae.pth.tar), [prior_level_0.pth.tar](https://openaipublic.azureedge.net/jukebox/models/5b/prior_level_0.pth.tar), [prior_level_1.pth.tar](https://openaipublic.azureedge.net/jukebox/models/5b/prior_level_1.pth.tar) and put them to `~/.cache/jukebox/models/5b`
and [prior_level_2.pth.tar](https://openaipublic.azureedge.net/jukebox/models/5b_lyrics/prior_level_2.pth.tar) to `~/.cache/jukebox/models/5b_lyrics`
```bash
python3_music generate_music.py --music_genre country               \
                                --artist john_denver                \
                                --save_path ./output/music          \
                                --sample_len 30
```

# Part 3

### Video generation

After music generation you will have three different musics `./output/music/item_0.wav`, `./output/music/item_1.wav`, `./output/music/item_2.wav`, so you will need to choose one and pass it to --music_filename

```bash
python3_video generate_video.py --frame_dir ./output/frames                       \
                                --tts_dir ./output/tts                            \
                                --music_filename ./output/music/item_0.wav        \
                                --temp_dir ./tmp                                  \
                                --video_name ./output/video/video.avi             \
                                --quality 6                                       \
                                --music_corrector -3
```