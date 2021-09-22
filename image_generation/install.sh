#!/bin/bash
cd "$(dirname "$0")"

pip install -r requirements.txt
git submodule update --init --recursive
cd diffvg
python setup.py install
cd ..