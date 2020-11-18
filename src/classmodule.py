"""
An extremely simple (useless) class that is imported into main.py and instantiated there. 
Again, this is just to show the how of importing a class from a module in the same package.

"""

class MyClass():
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print('name is {}'.format(self.name))
