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

## Authenticate with Google Analytics

To work with Google Analytics through Pandas's reader you first need to authenticate. This is a bit of round about process.

1. Go to the [Google API Console](https://code.google.com/apis/console)
2. Click the 'Services' tab and switch on 'Analytics API'
3. Click the 'API Access' tab and create a 'Create OAuth2.0 client ID'
4. Select 'Installed application'
5. Download the json and save in the root of dora.
6. ssh onto the vm.
7. From the root of dora (`/var/dora`) run `python authenticate.py`
8. Load the presented URL in a browser, authenticate and then copy the resulting URL (should start with localhost:8080)
9. In the vm curl the url with `curl [the url]`

[Do some Google Analytics magic](http://quantabee.wordpress.com/2012/12/17/google-analytics-pandas/)
