# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import piExp
version = piExp.__version__

setup(
    name='piExp',
    version=version,
    author='',
    author_email='xyloeric@gmail.com',
    packages=[
        'piExp',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['piExp/manage.py'],
)