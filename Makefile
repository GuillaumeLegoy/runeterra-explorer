.PHONY: clean lint requirements

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = runeterra-tracker
PYTHON_INTERPRETER = python3

requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pipenv
	$(PYTHON_INTERPRETER) -m pipenv install --dev

lint:
	pipenv run flake8 src

setup:
	pipenv run pipenv-setup sync --pipfile
