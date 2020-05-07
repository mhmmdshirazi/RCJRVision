#!/bin/bash
set -e
set -x

PYTHON_COMMAND=python
PIP_COMMAND=pip
if [ "$TRAVIS_OS_NAME" == "osx" ]
then
    PYTHON_COMMAND=python3
    PIP_COMMAND=pip3
fi

$PIP_COMMAND install -r requirements.txt
$PIP_COMMAND install RCJRVision

