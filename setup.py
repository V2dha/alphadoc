from setuptools import setup, find_packages
  
long_description = '''Automatic docstring generator and style guide that 
                    supports a number of specified conventions for formatting 
                    as well as documentation in Python.''' 
  
setup( 
        name ='alphacode', 
        version ='0.0.1',  
        url ='https://github.com/MLH-Fellowship/alphacode', 
        description ='Automatic style guide and docstrings generator for Python code', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'alphacode = alphacode.main:main'
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
            "autopep8==1.5.4"],
        zip_safe = False
) 