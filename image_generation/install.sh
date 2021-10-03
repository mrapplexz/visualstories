#!/bin/bash

pip install -r requirements.txt
pip install -e perlin-numpy
cd diffvg
python setup.py install
cd ..