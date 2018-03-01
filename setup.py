#!/usr/bin/python3
# bumpercare/setup.py

""" Setuptools project configuration for bumpercare. """

from os.path import exists
from setuptools import setup

LONG_DESC = None
if exists('README.md'):
    with open('README.md', 'r') as file:
        LONG_DESC = file.read()

setup(name='bumpercare',
      version='0.0.8',
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      long_description=LONG_DESC,
      packages=['bumpercare'],
      package_dir={'': 'src'},
      py_modules=[],
      include_package_data=False,
      zip_safe=False,
      scripts=[],
      description='BumperWare server',
      url='https://jddixon.github.io/bumpercare',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 2.7',
          'Programming Language :: Python 3.5',
          'Programming Language :: Python 3.6',
          'Programming Language :: Python 3.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
