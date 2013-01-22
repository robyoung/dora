# Dora

The Government data explorer.

This is an environment and set of tools for exploring data coming out of GDS. It is built
around the fantastic [IPython Notebook](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html).
Notebooks will be saved in the `notebooks` directory.

# Installation

## Requirements

You must have [Python 2.7+](http://www.python.org/) installed along with [virtualenv](http://www.virtualenv.org/en/latest/).
Note, that to render graphs directly in IPython you must be able to install [PyLab](http://www.scipy.org/PyLab). This can be
a pain on Mac OS X so it may be easier to run this from inside a Linux virtual machine.

## Setup

Clone this repository.

Run `start-ipython.sh`. The first time you run this it will take a while. It creates a virtual environment, installs the
requirements and starts IPython.

Navigate to `http://hostname:5555`

## Authenticate

There are notebooks created to help you authenticate with various APIs. They all start with 'AUTH', for example 'AUTH Google Analytics'.

