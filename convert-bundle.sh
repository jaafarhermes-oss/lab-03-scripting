#!/bin/bash

set -euo pipefail

curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz

tar -xzf lab3-bundle.tar.gz

awk 'NF > 0' lab3_data.tsv > cleaned_data.tsv

tr '\t' ',' < cleaned_data.tsv > lab3_data.csv

ROWS=$(tail -n +2 lab3_data.csv | wc -l)

echo "Number of data rows: $ROWS"

tar -czf converted-archive.tar.gz lab3_data.csv