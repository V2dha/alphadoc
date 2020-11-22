# alphacode
Automatic docstring generator and style guide that supports a number of specified conventions for formatting as well as documentation in Python.

Installation
------------

    $ pip install alphacode

Usage
-----
code-style takes your filename and format type as arguments

    $ alphacode --f <filename> --d <doc_format>

See `alphacode --help` for more command-line switches and options!

Features
--------
* Automatically fixes the code according to the style convention specified by the user.
* Auto-generates docstrings with a customizable template for functions and classes.
* Support for popular python convention styles such as PEP-8 and PEP-257
* Support for common and widely used docstrings formats such as Numpy, Google, ReStructured Text and Epytext (Javadoc)

Development
-----------
Check [CONTRIBUTING.md](CONTRIBUTING.md) for hacking details.
