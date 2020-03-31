#!/bin/bash
  set -e
  set -x
  IS_IN_TRAVIS=false
  PYTHON_COMMAND=python
  
  if [ "$TRAVIS_OS_NAME" == "osx" ]
  then
	PYTHON_COMMAND=python3
  fi
  $PYTHON_COMMAND -m scripts/main.py
