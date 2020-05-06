#!/bin/bash
  set -e
  set -x
  IS_IN_TRAVIS=false
  PYTHON_COMMAND=python
  
  if [ "$TRAVIS_OS_NAME" == "osx" ]
  then
	PYTHON_COMMAND=python3
  fi
  cd Example
  $PYTHON_COMMAND main.py
