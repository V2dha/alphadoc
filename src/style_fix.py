from os import listdir, walk
from os.path import isfile, join
import autopep8

class StyleFix:
    def __init__(self, directory='./', isWalk=False, options={}):
        self.directory = directory
        self.options = options
        self.isWalk = isWalk
        if not walk:
            self.python_files = [f for f in listdir(directory) if isfile(join(directory, f)) and f[-3:] == '.py']
        else:
            self.python_files = []
            for (dirpath, dirnames, filenames) in walk(directory):
                self.python_files.extend([f for f in filenames if f[-3:] == '.py'])
                
                
        
    def format_pep8(self):
        for file in self.python_files:
            content = ""
            
            with open(join(self.directory,file), 'r') as f:
                content = f.read()
                
            formatted = autopep8.fix_code(content, self.options)

            print(formatted)
            
            with open(join(self.directory,file), 'w') as f:
                f.write(formatted)
                
        

