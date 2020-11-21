import ast
import os

ast_filename = 'func.py'

with open(ast_filename) as fd:
    file_contents = fd.read()

module = ast.parse(file_contents)
function_definitions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

pos = []
for f in function_definitions:
    pos.append(f.lineno) 
    print(f.lineno, f.end_lineno, f.name)

string = '''    """
        This is an example of Google style.
        
        Args:
        param1: This is the first param.
        param2: This is a second param.

        Returns:
        This is a description of what is returned.

        Raises:
        KeyError: Raises an exception.
    """  '''

file = open(ast_filename, "r")
contents = file.readlines()
file.close()
j=0
for i in pos:
    contents.insert(i+j, string)
    j+=1

file = open(ast_filename, "w")
contents = " ".join(contents)
file.write(contents)
file.close()


