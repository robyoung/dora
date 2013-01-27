import os

import stats
ROOT_PATH=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def data_path(filename):
  return os.path.join(ROOT_PATH, "data", filename)
