# VideoStories generation

# Part 0

## Preparation
```
git clone git@github.com:mrapplexz/aiijc-creative-imagegen.git
cd aiijc-creative-imagegen
./install.sh
```

# Part 1

## Text generation

If your host doesn't provide access to huggingface hub, download 
`pytorch_model.bin`,`tokenizer_config.json`,`vocab.json`,`config.json`,`special_tokens_map.json`, `merges.txt` [here](https://huggingface.co/EleutherAI/gpt-neo-2.7B) before
and start with  `--local_model MODEL_PATH`
```
text_generation/text_generation_env/bin/python3 generate_text.py --device cuda:0                             \
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

## TTS generation

Before start you need to download pretrained model `LibriTTS_800000.tar`
[here](https://drive.google.com/drive/folders/1DOhZGlTLMbbAAFZmZGDdc77kz1PloS7F)
and put it to `./tts_generation/FastSpeech2/output/ckpt/LibriTTS/800000.pth.tar`

If your host doesn't provide access to nltk hub, you need to install `cmudict` and `averaged_perceptron_tagger` packages manually with [this instruction](http://www.nltk.org/data.html) 
```
tts_generation/tts_generation_env/bin/python3 generate_tts.py --input_filename ./output/texts/text.txt 
                                                              --temp_dir ./tmp
                                                              --speaker_id 205
                                                              --output_dir ./output/tts
```

# Part 3

## Frames generation

```
image_generation/image_generation_env/bin/python3 generate_images.py --input_filename ./output/texts/text.txt 
                                                                     --devices cuda:0,cuda:1
                                                                     --main_dir ./output/frames
```

# Part 4

## Music generation

```
cd music_generation
./install.sh
cd ..
python3 generate_music.py country john_denver
```

# Part 5

## Video generation

```
cd video_generation
./install.sh
cd ..
python3 generate_video.py ./frames ./tts ./music ./tmp/prepared_frames ./video/video.avi
```