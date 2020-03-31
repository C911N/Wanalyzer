#!/bin/sh

# Clean the repository

if [ "$1" ]; then
    WHERE="$1"
else
    WHERE="$PWD"
fi

find "$WHERE" \
    -name '__pycache__' -delete -print \
    -o \
    -name '*.pyc' -delete -print \
    -o \
    -name '.DS_Store' -delete -print \
    -o \
    -name '.mypy_cache' -print -exec rm -rf '{}' \; \
    -o \
    -name 'build' -print -exec rm -rf '{}' \; \
    -o \
    -name '*.egg-info' -print -exec rm -rf '{}' \; \
    -o \
    -name 'dist' -print -exec rm -rf '{}' \;
