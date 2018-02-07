#!/bin/bash

set -e
pip install -r docs-requirements.txt
cd docs
make html
cd ..
python -m doctr deploy docs

python -m doctr deploy --sync --require-master  --built-docs docs/_build/html "."
python -m doctr deploy --sync --no-require-master  --built-docs docs/_build/html "docs-$TRAVIS_BRANCH"
