#!/bin/bash
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate  -i swagger.json -l python -o /local -DprojectName=pyrebrickable -DpackageName=rebrickable