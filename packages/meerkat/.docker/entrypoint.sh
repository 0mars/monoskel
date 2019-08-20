#!/bin/sh

pip install -r requirements.txt
pip install -r requirements-dev.txt

# install other packages
cd ../../ && yarn bootstrap && cd packages/meerkat

# nodemon catches crashes, known issue: double watch files
nodemon -e py --watch src/meerkat --exec make run
# make run
