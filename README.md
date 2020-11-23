# alphadoc
Automatic docstring generator and style guide that supports a number of specified conventions for documentation in Python.

Installation
------------
Using pip:

    $ pip install alphadoc
    
Using local build:

    $ git clone https://github.com/MLH-Fellowship/alphadoc.git
    $ pip install -e .
    $ python setup.py install
    $ python setup.py sdist bdist_wheel

Usage
-----
alphadoc takes your filename and format type as arguments

    $ alphadoc <filename> --d <doc_format>

See `alphadoc --help` for more command-line switches and options!

Features
--------
* Auto-generates docstrings with a customizable template for functions and classes.
* Automatically fixes the code according to the standard PEP-8 style convention for python.
* Support for common and widely used docstrings formats such as Numpy, Google, ReStructured Text and Epytext (Javadoc)

Contributing
-----------
alphadoc is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [CONTRIBUTING.md](CONTRIBUTING.md)
