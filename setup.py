from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')  
 
  
setup( 
        name ='alphadoc', 
        version ='1.0.1',  
        url ='https://github.com/MLH-Fellowship/alphadoc', 
        description ='Automatic style guide and docstrings generator for Python code', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'alphadoc = alphadoc.main:main'
            ] 
        }, 
        classifiers =[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Documentation'
        ], 
        keywords ='automation, docstring-generator, auto-docstrings, pep8', 
        install_requires = [
            "click==7.1.2", 
            "setuptools==50.3.2", 
            "autopep8==1.5.4",
            "pathlib==1.0.1"],
        zip_safe = False
) 