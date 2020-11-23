import click
import autopep8
from alphadoc.docstring import get_docstring
from alphadoc.style_fix import StyleFix

info = '''Automatic docstring generator and style guide that 
          supports a number of specified conventions for formatting 
          as well as documentation in Python.'''

doc_help = '''Specified format for docstrings from Options-
                                ReST : For ReStructured Text (default);
                        Epytext :  For Epytext (Javadoc);
                        Google : For Google-Style ;
                        Numpydoc : For Numpydoc'''
@click.command(help=info)
@click.argument('filename')
@click.option('--doc_format', '-d', default='ReST', help=doc_help)

def main(filename, doc_format):
    get_docstring(filename, doc_format)

if __name__ == "__main__" :
    main()