#!/bin/sh

# Run Wanalyzer tests with Python 3

PYTHON_VERSION=$(python -c 'import platform; print(platform.python_version())')
PYTHON_BIN=python

if [[ $PYTHON_VERSION == 2.* ]]; then
    PYTHON_BIN=python3
fi

$PYTHON_BIN -m unittest discover tests "*_tests.py" -v