# put env TWINE_REPOSITORY_URL=https://test.pypi.org/legacy/ for testing

.PHONY: clean

TAG_NAME:=${TAG_NAME}
VERSION ?= $(if $(TAG_NAME),$(TAG_NAME),dev)

swagger.json: rebrickable.json
	pipenv run patch_swagger.py
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
	make -C docs html
