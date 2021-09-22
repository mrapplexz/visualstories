# VideoStories generation

# Part 1

## Text generation

```
cd text_generation
./install.sh
cd ..
python3 generate_text.py cuda:0 ./texts/text.txt 
```

# Part 2

## TTS generation

Before start you need to download pretrained model `LibriTTS_800000.pth.tar`
[here](https://drive.google.com/drive/folders/1DOhZGlTLMbbAAFZmZGDdc77kz1PloS7F)
and put it to `./tts_generation/FastSpeech2/output/ckpt/LibriTTS/800000.pth.tar`

```
cd tts_generation
./install.sh
cd ..
python3 generate_tts.py ./texts/text.txt ./tmp/source.txt 205 ./tts
```

# Part 3

## Frames generation

```
cd image_generation
./install.sh
cd ..
python3 generate_images.py ./texts/text.txt cuda:0,cuda:1 ./frames
```

# Part 4

## Music generation

```
cd music_generation
./install.sh
cd ..
python3 generate_music.py country john_denver
```
