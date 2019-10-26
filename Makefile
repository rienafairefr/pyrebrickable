# put env TWINE_REPOSITORY_URL=https://test.pypi.org/legacy/ for testing

.PHONY: clean

TAG_NAME:=${TAG_NAME}
VERSION ?= $(if $(TAG_NAME),$(TAG_NAME),dev)

deploy_pypi:
ifdef VERSION
	rm -rf dist

	python3 api/setup.py sdist bdist_wheel
	python3 cli/setup.py sdist bdist_wheel
	python3 data/setup.py sdist bdist_wheel
	python3 setup.py sdist bdist_wheel

	twine upload -u ${PYPI_USER} -p ${PYPI_PASSWORD} dist/*
else
	@echo "not tagged"
endif

swagger.json: rebrickable.json
	python3 patch_swagger.py
	echo -- `cat swagger.json`

clean:
	rm -rf rebrickable/api

rebrickable/api: swagger.json Makefile
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.3 \
	           generate \
	           -g python \
	           -i /local/swagger.json \
	           -o /local \
	           --git-user-id rienafairefr \
	           --git-repo-id pyrebrickable \
	           -p generateSourceCodeOnly=true \
	           -p packageName=rebrickable.api \



build_docs:
	set -e
	pip3 install -r docs-requirements.txt
	make -C docs html

deploy_docs: build_docs
	#python -m doctr deploy docs

	#python -m doctr deploy --sync --require-master  --built-docs docs/_build/html "."
	#python -m doctr deploy --sync --no-require-master  --built-docs docs/_build/html "docs-$(TRAVIS_BRANCH)"
