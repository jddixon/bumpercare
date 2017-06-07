#!/usr/bin/python3
# ~/dev/py/bumpercare/setup.py

""" Set up distutils for bumpercare. """

import re
from distutils.core import setup
__version__ = re.search(r"__version__\s*=\s*'(.*)'",
                        open('src/bumpercare/__init__.py').read()).group(1)

# see http://docs.python.org/distutils/setupscript.html

setup(name='bumpercare',
      version=__version__,
      author='Jim Dixon',
      author_email='jddixon@gmail.com',
      #
      # wherever we have a .py file that will be imported, we
      # list it here, without the .py extension but SQuoted
      py_modules=[],
      #
      packages=['src/bumpercare', ],
      #
      # following could be in scripts/ subdir; SQuote
      scripts=[],
      description='default proj desc',
      url='https://jddixon/github.io/bumpercare',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python 3',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],)
