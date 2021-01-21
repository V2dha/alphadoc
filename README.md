# alphadoc

[![PyPI version](https://img.shields.io/pypi/v/alphadoc.svg?color=green&style=for-the-badge)](https://pypi.org/project/pdoc3)
![ISSUES](https://img.shields.io/github/issues-closed/MLH-Fellowship/alphadoc?color=blue&style=for-the-badge)
![PULL REQUESTS](https://img.shields.io/github/issues-pr-closed/MLH-Fellowship/alphadoc?color=orange&style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/alphadoc?style=for-the-badge)
    
Automatic docstring generator and style guide that supports a number of specified conventions for documentation in Python.

Features
--------
* Auto-generates docstrings with a customizable template for functions.
* Automatically fixes the code according to the standard PEP-8 style convention for python.
* Support for common and widely used docstrings formats such as Numpy, Google, ReStructured Text and Epytext (Javadoc)

Installation
------------
Using pip:

    $ pip install alphadoc

Usage
-----
alphadoc takes your filename and format type as arguments

    $ alphadoc <filename> -d <doc_format>

See `alphadoc --help` for more command-line switches and options!

Options :
```
Usage: alphadoc [OPTIONS] FILENAME

  Automatic docstring generator and style guide that  supports a
  number of specified conventions for formatting  as well as
  documentation in Python.

Options:
  -d, --doc_format TEXT  Specified format for docstrings from Options-
                         ReST : For ReStructured Text (default); Epytext
                         :  For Epytext (Javadoc); Google : For Google-
                         Style ; Numpydoc : For Numpydoc

  --help                 Show this message and exit.
```
Example :

Before alphadoc
```python
import ast
import sys

def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def get_func(filename):
    tree = parse_ast(filename)
    func_list = []
    for func in top_level_functions(tree.body):
        func_list.append(func.name)
    return func_list
```
After alphadoc 

Docstring format:

* **ReStructured Text** (default) 
```python
import ast
import sys

def top_level_functions(body):
    """
        This is reST style.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
    """
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    """
        This is reST style.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
    """
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def get_func(filename):
    """
        This is reST style.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
    """
    tree = parse_ast(filename)
    func_list = []
    for func in top_level_functions(tree.body):
        func_list.append(func.name)
    return func_list
```
* **Epytext (Javadoc)** 
```python
import ast
import sys

def top_level_functions(body):
    """
        This is javadoc style.

        @param param1: this is a first param
        @param param2: this is a second param
        @return: this is a description of what is returned
        @raise keyError: raises an exception
    """
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    """
        This is javadoc style.

        @param param1: this is a first param
        @param param2: this is a second param
        @return: this is a description of what is returned
        @raise keyError: raises an exception
    """
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def get_func(filename):
    """
        This is javadoc style.

        @param param1: this is a first param
        @param param2: this is a second param
        @return: this is a description of what is returned
        @raise keyError: raises an exception
    """
    tree = parse_ast(filename)
    func_list = []
    for func in top_level_functions(tree.body):
        func_list.append(func.name)
    return func_list
```
* **Google** 
```python
import ast
import sys

def top_level_functions(body):
    """
            This is an example of Google style.
            
            Args:
            param1: This is the first param.
            param2: This is a second param.

            Returns:
            This is a description of what is returned.

            Raises:
            KeyError: Raises an exception.
    """
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    """
            This is an example of Google style.
            
            Args:
            param1: This is the first param.
            param2: This is a second param.

            Returns:
            This is a description of what is returned.

            Raises:
            KeyError: Raises an exception.
    """
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def get_func(filename):
    """
            This is an example of Google style.
            
            Args:
            param1: This is the first param.
            param2: This is a second param.

            Returns:
            This is a description of what is returned.

            Raises:
            KeyError: Raises an exception.
    """
    tree = parse_ast(filename)
    func_list = []
    for func in top_level_functions(tree.body):
        func_list.append(func.name)
    return func_list
```
* **Numpydoc** 
```python
import ast
import sys

def top_level_functions(body):
    """
        Numpydoc description of a kind
        of very exhautive numpydoc format docstring.

        Parameters
        ----------
        first : array_like
            the 1st param name `first`
        second :
            the 2nd param
        third : {'value', 'other'}, optional
            the 3rd param, by default 'value'

        Returns
        -------
        string
            a value in a string

        Raises
        ------
        KeyError
            when a key error
        OtherError
            when an other error
    """
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    """
        Numpydoc description of a kind
        of very exhautive numpydoc format docstring.

        Parameters
        ----------
        first : array_like
            the 1st param name `first`
        second :
            the 2nd param
        third : {'value', 'other'}, optional
            the 3rd param, by default 'value'

        Returns
        -------
        string
            a value in a string

        Raises
        ------
        KeyError
            when a key error
        OtherError
            when an other error
    """
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

def get_func(filename):
    """
        Numpydoc description of a kind
        of very exhautive numpydoc format docstring.

        Parameters
        ----------
        first : array_like
            the 1st param name `first`
        second :
            the 2nd param
        third : {'value', 'other'}, optional
            the 3rd param, by default 'value'

        Returns
        -------
        string
            a value in a string

        Raises
        ------
        KeyError
            when a key error
        OtherError
            when an other error
    """
    tree = parse_ast(filename)
    func_list = []
    for func in top_level_functions(tree.body):
        func_list.append(func.name)
    return func_list
```

References
-----------
http://daouzli.com/blog/docstring.html


Contributing
-----------
alphadoc is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [CONTRIBUTING.md](CONTRIBUTING.md)

## Contributors 

Thanks goes to these wonderful people ⭐ 
<table>
  <!--- Row 1 --->
	<tr>
        <td align="center">
            <a href="https://github.com/V2dha">
              <img src="https://avatars1.githubusercontent.com/u/50369708?v=4" width="100px" alt=""/><br />
              <sub><b>V2dha</b></sub>
            </a><br/>
            <a href="https://github.com/MLH-Fellowship/alphadoc/commits?author=V2dha">
                💻 📖 👀 📆 💬 
            </a>
          </td>
        <td align="center">
            <a href="https://github.com/eamspoker">
              <img src="https://avatars1.githubusercontent.com/u/46005655?v=4" width="100px" alt=""/><br />
              <sub><b>eamspoker</b></sub>
            </a><br/>
            <a href="https://github.com/MLH-Fellowship/alphadoc/commits?author=eamspoker">
                💻 🤔 
            </a>
          </td>
        <td align="center">
            <a href="https://github.com/akrish4">
              <img src="https://avatars0.githubusercontent.com/u/61831021?v=4" width="100px" alt=""/><br />
              <sub><b>akrish4</b></sub>
            </a><br/>
            <a href="https://github.com/MLH-Fellowship/alphadoc/commits?author=akrish4">
                📖
            </a>
          </td>
     </tr>
</table>
