#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='plotkit',
    version='0.0.5',
    author='Martok',
    description='Collection of helpers for plotting with matplotlib',
    url='https://github.com/martok/py-plotkit',
    packages=find_packages(),
    install_requires=[
        'matplotlib'
    ],
    python_requires='>=3.6',
)
