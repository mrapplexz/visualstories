#!/bin/bash
cd "$(dirname "$0")"

pip install -r requirements.txt
git submodule init --recursive
cd diffvg
git submodule update --init --recursive
python setup.py install
cd ..