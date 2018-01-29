#!/bin/bash
rm -rf docs
rm -rf rebrickable/api
rm -rf rebrickable/models
docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/swagger.json -l python -o /local -DprojectName=pyrebrickable -DpackageName=rebrickable