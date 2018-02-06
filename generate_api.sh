#!/bin/bash
echo -- `cat swagger.json`

docker run --rm --user `id -u`:`id -g` -v ${PWD}:/local swaggerapi/swagger-codegen-cli\
              generate -i /local/swagger.json\
              --git-user-id rienafairefr\
              --git-repo-id pyrebrickable\
              -l python -o /local/pyrebrickable-api -DprojectName=pyrebrickable_api -DpackageName=rebrickable_api\
              -DpackageVersion="`cat VERSION`"