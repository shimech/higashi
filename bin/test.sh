#!/bin/sh

if [ $# -eq 0 ]; then
    FILES=./src/*/test.py
    for file in ./src/*/test.py; do
        echo "### Testing $file ... ###"
        pipenv run python $file -v
    done
else
    for dir in "$@"; do
        file=./src/$dir/test.py
        if [ -e $file ]; then
            echo "### Testing $file ... ###"
            pipenv run python $file -v
        else
            echo "$file is NOT found."
        fi
    done
fi
