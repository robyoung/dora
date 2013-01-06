#! /usr/bin/env sh

if [ ! -d venv ]; then
  virtualenv --no-site-packages venv

  source venv/bin/activate

  pip install -r requirements.txt
fi
