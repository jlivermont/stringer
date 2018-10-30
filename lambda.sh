#!/bin/bash

set -ex

cp app/validators/all_letters.py .
zip lambda.zip all_letters.py
rm all_letters.py

set +e
aws lambda delete-function --function-name all-letters-validator
set -e

aws lambda create-function --region us-west-2 \
  --function-name all-letters-validator --zip-file fileb://lambda.zip \
  --role "arn:aws:iam::846025239765:role/jlivermont-api-role" \
  --handler all_letters.all_letters_validator_lambda --runtime python3.6

rm lambda.zip

aws lambda invoke --invocation-type RequestResponse --function-name all-letters-validator \
  --region us-west-2 --log-type Tail \
  --payload '{"string": "abcdefg"}' output.txt

grep 'false' output.txt

aws lambda invoke --invocation-type RequestResponse --function-name all-letters-validator \
  --region us-west-2 --log-type Tail \
  --payload '{"string": "abcdefghijklmnopqrstuvwxyz"}' output.txt

grep 'true' output.txt
