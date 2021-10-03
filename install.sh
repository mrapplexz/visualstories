#!/bin/bash

# submodules
git submodule update --init --recursive

# output and tmp
mkdir output
mkdir tmp

# text
python3 -m venv text_generation/text_generation_env
text_generation/text_generation_env/bin/pip3 install -r text_generation/requirements.txt
mkdir output/texts

# tts
python3 -m venv tts_generation/tts_generation_env
tts_generation/tts_generation_env/bin/pip3 install -r tts_generation/requirements.txt
unzip tts_generation/FastSpeech2/hifigan/generator_universal.pth.tar -d tts_generation/FastSpeech2/hifigan/
mkdir output/tts

# image
python3 -m venv image_generation/image_generation_env
image_generation/image_generation_env/bin/pip3 install -r image_generation/requirements.txt
image_generation/image_generation_env/bin/pip3 install -e image_generation/perlin-numpy
image_generation/image_generation_env/bin/pip3 install -e image_generation/diffvg
mkdir output/frames

