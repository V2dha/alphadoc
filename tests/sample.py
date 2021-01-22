import ast

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







