#!/bin/sh

if [ $# -lt 1 ]; then
    echo "Please select a directory."
    exit 1
fi

pipenv run python ./$1/test.py -v
