#!/bin/bash

pip install -r requirements.txt
git submodule update --init --recursive
cd diffvg
python setup.py install
cd ..