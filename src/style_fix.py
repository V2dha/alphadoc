from os import listdir
from os.path import isfile, join
import autopep8

class Style_Fix:
    def __init__(self, directory='../test', walk=False):
        self.directory = directory
        self.walk = walk
        if not walk:
            self.python_files = [f for f in listdir(directory) if isfile(join(directory, f)) and f[-3:] == '.py']
        else:
            pass
        
    def format_python(self):
        for file in self.python_files:
            content = ""
            
            with open(join(self.directory,file), 'r') as f:
                content = f.read()
                
            formatted = autopep8.fix_code(content)

            print(formatted)
            
            with open(join(self.directory,file), 'w') as f:
                f.write(formatted)
        
