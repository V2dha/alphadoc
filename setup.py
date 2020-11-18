from setuptools import setup, find_packages
import requirements

install_requires = []

with open('requirements.txt', 'r') as fd:
    for req in requirements.parse(fd):
        if req.name:
            name = req.name.replace("-", "_")
            full_line = name + "".join(["".join(list(spec)) for spec in req.specs])
            install_requires.append(full_line)
  
long_description = 'Description of the python package' 
  
setup( 
        name ='name-of-the-package', 
        version ='0.0.1',  
        url ='https://github.com/MLH-Fellowship/python-cli', 
        description ='Python Cli Package', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'python-cli = src.main:main'
            ] 
        }, 
        classifiers =[
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ], 
        keywords ='', 
        install_requires = install_requires,
        zip_safe = False
) 