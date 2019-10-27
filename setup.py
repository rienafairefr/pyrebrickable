# coding: utf-8
"""
pyrebrickable setup.py
"""

import os

from setuptools import setup

NAME = "pyrebrickable"
VERSION = os.environ.get('TAG_NAME', 'dev')


REQUIRES = ["decorator", 'appdirs', 'enum34', 'PyYaml', 'sqlalchemy',
            "click >=6", "urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    long_description="""This is pyrebrickable, tools for the www.rebrickable.com website and data
    
It provides:
* an auto-generated rebrickable API (in rebrickable.api)
* a CLI wrapper around that API (in rerickable.cli)
* a SQLalchemy wrapper around the monthly database dumps (in rebrickable.data)

It uses the monthly data dumps (http://www.rebrickable.com/downloads) and provides
SQLAlchemy models to query the data inside. Data is stored in a local SQLite file
in your user directory (inside %APPDATA% on Windows, ~/.local/share on Linux, ~/Library/Application Support/ on MacOS)

Once installed, you gain access to the rebrickable-data cli :

`rebrickable-data download` to download csv files from rebrickable
`rebrickable-data import` to import them in a database
`rebrickable-data reset-db` to reset the in a database
#EXPERIMENTAL# `rebrickable-data download-extra` to download data from rebrickable that are not in the dumps (e.g. MOCs data)

see examples in examples folder

""",
    long_description_content_type='text/markdown',
    author='rienafairefr',
    author_email="rienafairefr@gmail.com",
    url="https://rienafairefr.github.io/pyrebrickable/",
    entry_points={
        'console_scripts': [
            'rebrickable-data=rebrickable.data.cli:main',
            'rebrickable=rebrickable.cli.main:main'
        ]
    },
    keywords=["rebrickable"],
    install_requires=REQUIRES,
)
