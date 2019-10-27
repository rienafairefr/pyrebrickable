
.PHONY: clean

TAG_NAME:=${TAG_NAME}
VERSION ?= $(if $(TAG_NAME),$(TAG_NAME),dev)

swagger.json: rebrickable.json
	python patch_swagger.py
	echo -- `cat swagger.json`

clean:
	rm -rf rebrickable/api

rebrickable/api: swagger.json
	docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.3 \
	           generate \
	           -g python \
	           -i /local/swagger.json \
	           -o /local \
	           --git-user-id rienafairefr \
	           --git-repo-id pyrebrickable \
	           -p generateSourceCodeOnly=true \
	           -p packageName=rebrickable.api \
