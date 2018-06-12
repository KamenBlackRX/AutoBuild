import os
from os import path
from codecs import open
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

here = path.abspath(path.dirname(__file__))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '')
                    for x in all_reqs if x.startswith('git+')]


setup(
    name="AutoBuild",
    version="0.0.1",
    author="Jefferson Puchalski",
    author_email="puchiruzuki@gmail.com",
    description=(
        "A project to build and make any dev enviroment from a list."),
    license="MIT",
    keywords="build auto",
    url="http://packages.python.org/autobuild",
    
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires,
    long_description=read('README.md'),
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Development Status :: 6 - Mature",
        "Development Status :: 7 - Inactive",
        "Topic :: Utilities",
        "License :: MIT Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'autobuild = main:main'
        ]
    },
    


)
