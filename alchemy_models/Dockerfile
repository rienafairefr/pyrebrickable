FROM maven:3-jdk-8 as builder

COPY . /meta

RUN mvn -f /meta package

FROM openapitools/openapi-generator-cli:v3.3.4

COPY --from=builder /meta/target/alchemy-openapi-generator-1.0.0.jar /meta/

ENTRYPOINT java -cp /meta/alchemy-openapi-generator-1.0.0.jar:/opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar org.openapitools.codegen.OpenAPIGenerator
