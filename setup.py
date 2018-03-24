# coding: utf-8
"""
pyrebrickable setup.py
"""

import os

from setuptools import setup

NAME = "pyrebrickable"
VERSION = os.environ.get('TRAVIS_TAG', os.environ.get('TAG_NAME', 'dev'))


REQUIRES = ["pyrebrickable_api", "pyrebrickable_cli", "pyrebrickable_data"]

setup(
    name=NAME,
    version=VERSION,
    description="""This is pyrebrickable, tools for the www.rebrickable.com website and data
    
It provides:
* an auto-generated rebrickable API (in the rebrickable_api package)
* a CLI wrapper around that API (in the rerickable_cli package)
* a SQLalchemy wrapper around the monthly database dumps (in the rebrickable_data package)

""",
    author_email="",
    url="",
    keywords=["rebrickable"],
    install_requires=REQUIRES,
)
