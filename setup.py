#-*- coding:utf-8 -*-


import setuptools

version = '0.0.1'

setuptools.setup(
    name='scalalike.collections',
    packages=['scalalike.collections'],
    install_requires=[
        ],
    include_dirs=['test', 'test/*.py'],
    namespace_packages=['scalalike'],
    data_files=[
        ('test', ['test/*.py']),
        ],
    include=['test/*.py'],
    version=version)

