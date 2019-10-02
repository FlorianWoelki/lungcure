#!/bin/bash

git pull &&
source ./bin/activate &&

python3 -m flask run
