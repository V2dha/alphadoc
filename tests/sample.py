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







