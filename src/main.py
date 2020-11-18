#entry point for the CLI indicated by the setup config in setup.py  
"""
All this does is import a few other modules in the src dir, 
parse args passed to the CLI, and implements those imported module members (a simple function and a simple class).

"""
import sys
from .classmodule import MyClass
from .funcmodule import my_function

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    my_function('hello world')

    my_object = MyClass('Vividha')
    my_object.say_name()

if __name__ == '__main__':
    main()