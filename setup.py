#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "longerusername",
    version = "0.4",
    url='http://github.com/GoodCloud/django-longer-username',
    packages = find_packages(),
    license = 'BSD',
    zip_safe = False,
)
