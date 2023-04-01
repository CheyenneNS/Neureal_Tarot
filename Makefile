PROJ_BASE=$(shell pwd)
APP_BASE=$(PROJ_BASE)
PYTHONVER=python3.8
PYTHONVENV=$(PROJ_BASE)/venv
SYSTEM_PYTHON=python3
INSTR_ENVIROMENT=app.env
VENVPYTHON=$(PYTHONVENV)/bin/python

RAND_HEX := $(shell openssl rand -hex 32)

.PHONY: install
install: bootstrap
	@echo "Installing Neureal Tarot"
	$(VENVPYTHON) setup.py install
	@echo "\nYou may want to activate the virtual environmnent with 'source venv/bin/activate'\n"

.PHONY: develop
develop: bootstrap
	@echo "Installing Neureal Tarot, with editible modules ('python setup.py develop')"
	$(VENVPYTHON) setup.py develop
	@echo "\nYou may want to activate the virtual environmnent with 'source venv/bin/activate'\n"

.PHONY: bootstrap
bootstrap:
	@echo "Creating virtual environment 'venv' for development."
	$(SYSTEM_PYTHON) -m virtualenv -p $(PYTHONVER) venv
	@echo "Installing python modules from requirements.txt"
	$(VENVPYTHON) -m pip install -r requirements.txt


.PHONY: clean_build
clean_build:
	@echo "Removing build artifacts"
	rm -rf $(PROJ_BASE)/build
	rm -rf $(PROJ_BASE)/dist
	rm -rf $(PROJ_BASE)/*.egg-info
	rm -rf $(PROJ_BASE)/docs/_build/*

.PHONY: clean
clean: clean_build
	@echo "Removing Python virtual environment 'venv'."
	rm -rf $(PYTHONVENV)

.PHONY: sparkling
sparkling: clean
	rm -rf *.whl
	find . -name \*~ | xargs rm -f
	rm -rf dist build src/*.egg-info
	rm -rf **/__pycache__
	rm -rf docs/_build/*
	rm -f src/version.py
	rm -rf htmlcov
	rm -rf .tox
	rm -rf .pytest_cache