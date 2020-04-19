#!/bin/sh

if [ $# -lt 1 ]; then
    echo "Please select directories."
    exit 1
fi

for TEST_DIR in "$@"
do
    echo "### Testing ${TEST_DIR}... ###"
    pipenv run python ./$TEST_DIR/test.py -v
done
