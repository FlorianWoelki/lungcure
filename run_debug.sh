#!/bin/bash

git pull &&
source ./bin/activate &&

export FLASK_DEBUG=1 &&
python3 -m flask run
