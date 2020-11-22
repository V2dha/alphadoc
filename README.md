# alphacode
Automatic docstring generator and style guide that supports a number of specified conventions for formatting as well as documentation in Python.

Installation
------------
Using pip:

    $ pip install alphacode
    
Using local build:

    $ git clone https://github.com/MLH-Fellowship/alphacode.git
    $ pip install -e .
    $ python setup.py install
    $ python setup.py sdist bdist_wheel

Usage
-----
code-style takes your filename and format type as arguments

    $ alphacode <filename> --d <doc_format>

See `alphacode --help` for more command-line switches and options!

Features
--------
* Automatically fixes the code according to the style convention specified by the user.
* Auto-generates docstrings with a customizable template for functions and classes.
* Support for popular python convention styles such as PEP-8 and PEP-257
* Support for common and widely used docstrings formats such as Numpy, Google, ReStructured Text and Epytext (Javadoc)

Contributing
-----------
alphacode is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [CONTRIBUTING.md](CONTRIBUTING.md)
