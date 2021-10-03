#!/bin/bash

# submodules
git submodule update --init --recursive

# output
mkdir output

# text
python3 -m venv text_generation/text_generation_env
text_generation/text_generation_env/bin/pip3 install -r text_generation/requirements.txt
mkdir output/texts

