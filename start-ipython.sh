#! /usr/bin/env sh

sh setup.sh

source venv/bin/activate
PYTHONPATH=`pwd` ipython notebook --port=5555 --ip='*' --notebook-dir=notebooks
