import ast
import os

def get_docstring(ast_filename, doc_format):
    rest = '''    """
        This is reST style.

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
    """\n'''

    google = '''    """
            This is an example of Google style.
            
            Args:
            param1: This is the first param.
            param2: This is a second param.

            Returns:
            This is a description of what is returned.

            Raises:
            KeyError: Raises an exception.
    """\n'''

    epytext = '''    """
        This is javadoc style.

        @param param1: this is a first param
        @param param2: this is a second param
        @return: this is a description of what is returned
        @raise keyError: raises an exception
    """\n'''

    numpydoc = '''    """
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
    """\n'''

    with open(ast_filename) as fd:
        file_contents = fd.read()

    module = ast.parse(file_contents)
    function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

    pos = []
    k = 0
    for f in function_definitions:
        k+=1
        pos.append(f.lineno) 
        print('Function {} : {}'.format(k, f.name))
        print('-----------------------')

    file = open(ast_filename, "r")
    contents = file.readlines()
    file.close()
    j=0
    for i in pos:
        if doc_format == 'ReST':
            contents.insert(i+j, rest)
        elif doc_format == 'Epytext':
            contents.insert(i+j, epytext)
        elif doc_format == 'Google':
            contents.insert(i+j, google)
        elif doc_format == 'Numpydoc':
            contents.insert(i+j, numpydoc)
        else:
            print('No such format exists!')
            break
        j+=1
    file = open(ast_filename, "w")
    contents = "".join(contents)
    file.write(contents)
    file.close()





