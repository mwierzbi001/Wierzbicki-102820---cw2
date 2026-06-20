#!/bin/bash

python3 -m venv .venv

source .venc/bin/activate

pip install --upgrade pip
pip install -r requirements.txt