#!/bin/bash
set -e
FULL_SPEC_PATH=`readlink -f $1`

# Idempotent, local library install
virtualenv venv
source venv/bin/activate
pip install swagger-spec-validator

# Test the Spec
python -c "from swagger_spec_validator import validate_spec_url; validate_spec_url('file://${FULL_SPEC_PATH}')"
