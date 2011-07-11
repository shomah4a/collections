#-*- coding:utf-8 -*-

import setuptools

from scalalike.collections import __version__, __author__, __doc__, __license__



setuptools.setup(
    name='scalalike.collections',
    version=__version__,
    author=__author__,
    author_email='shoma.h4a+pypi@gmail.com',
    license=__license__,
    url='https://github.com/shomah4a/collections',
    description='scala like collection interface for python iterable.',
    long_description=__doc__,
    packages=['scalalike.collections'],
    install_requires=[
        'setuptools',
        ],
    include_dirs=['test', 'test/*.py'],
    namespace_packages=['scalalike'],
    data_files=[
        ('test', ['test/*.py']),
        ],
    include=['test/*.py'],
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
'''.strip().splitlines())

