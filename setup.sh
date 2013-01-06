#! /usr/bin/env sh

if [ ! -d venv ]; then
  virtualenv --no-site-packages venv

  pip install -r requirements.txt
fi
