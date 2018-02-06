#!/bin/bash
if [[ "${TRAVIS_TAG}" != "" ]]; then

rm -rf dist

python pyrebrickable-api/setup.py sdist bdist_wheel
python pyrebrickable-cli/setup.py sdist bdist_wheel

twine upload -u $PYPI_USER -p $PYPI_PASSWORD dist/*

fi;