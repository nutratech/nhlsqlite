SHELL=/bin/bash

.DEFAULT_GOAL := _help

# NOTE: must put a <TAB> character and two pound "\t##" to show up in this list.  Keep it brief! IGNORE_ME
.PHONY: _help
_help:
	@printf "\nUsage: make <command>, valid commands:\n\n"
	@grep "##" $(MAKEFILE_LIST) | grep -v IGNORE_ME | grep -v '^#' | sed -e 's/##//' | column -t -s $$'\t'



# ---------------------------------------
# init & venv
# ---------------------------------------

.PHONY: init
init:	## Set up a Python virtual environment
	rm -rf .venv
	${PY_SYS_INTERPRETER} -m venv .venv
	- if [ -z "${CI}" ]; then ${PY_SYS_INTERPRETER} -m venv --upgrade-deps .venv; fi
	direnv allow

# include .env
SKIP_VENV ?=
PYTHON ?= $(shell which python)
PWD ?= $(shell pwd)
.PHONY: _venv
_venv:
	# Test to enforce venv usage across important make targets
	[ "${SKIP_VENV}" ] || [ "${PYTHON}" = "${PWD}/.venv/bin/python" ]



# ---------------------------------------
# Install requirements
# ---------------------------------------

PY_SYS_INTERPRETER ?=
ifeq ($(PY_SYS_INTERPRETER),)
	ifeq ($(OS),Windows_NT)
		PY_SYS_INTERPRETER += python3
	else
		PY_SYS_INTERPRETER += /usr/bin/python3
	endif
endif

PY_VIRTUAL_INTERPRETER ?= python
PIP ?= $(PY_VIRTUAL_INTERPRETER) -m pip

REQ_OPT := requirements-optional.txt
REQ_LINT := requirements-lint.txt
REQ_TEST := requirements-test.txt
REQ_TEST_OLD := requirements-test-old.txt

PIP_OPT_ARGS ?= $(shell if [ "$(SKIP_VENV)" ]; then echo "--user"; fi)

.PHONY: deps
deps: _venv	## Install requirements
	${PIP} install wheel
	- ${PIP} install ${PIP_OPT_ARGS} -r requirements.txt
	- ${PIP} install ${PIP_OPT_ARGS} -r ${REQ_LINT}



# ---------------------------------------
# Clean, format, lint
# ---------------------------------------

.PHONY: clean
clean:	## Clean up build intermediates
	- rm -i  sql/db.sqlite3
	rm -rf .mypy_cache/ .pytest_cache/
	find sql/ -name __pycache__ -o -name .pytest_cache | xargs rm -rf


LINT_LOCS_PY ?= sql/
LINT_LOCS_YAML ?= .github/
LINT_LOCS_RST ?= $(shell git ls-files \*.rst)

.PHONY: format
format:	## Format SQL files with pg_format
	black ${LINT_LOCS_PY}
	bash sql/format.sh
	- prettier --write ${LINT_LOCS_YAML}

.PHONY: lint
lint:	## Lint Python code
	black --check ${LINT_LOCS_PY}
	bandit -q -r ${LINT_LOCS_PY}
	pycodestyle ${LINT_LOCS_PY}
	flake8 ${LINT_LOCS_PY}
	pylint ${LINT_LOCS_PY}
	mypy ${LINT_LOCS_PY}
	# Lint YAML
	yamllint ${LINT_LOCS_YAML}
	prettier --check ${LINT_LOCS_YAML}
	# Lint RST
	doc8 -q ${LINT_LOCS_RST}



# ---------------------------------------
# Python build & install (test, docs)
# ---------------------------------------

.PHONY: build
build: _venv	## Build sqlite image
	python3 -m sql

.PHONY: test
test:	## Cursory sanity check
	sqlite3 -csv -header \
		sql/db.sqlite3 \
		"SELECT name, tbl_name, sql FROM sqlite_master WHERE type = 'index';" \
		'SELECT * FROM license;' \
		'SELECT * FROM version;' \
		'SELECT * FROM team;' \
		'SELECT * FROM game_type;' \
		'SELECT * FROM game;' \

.PHONY: docs
docs:	## Generate table diagram (requires sqleton)
	bash docs/sqleton.sh

PROJECT_PKG_NAME ?= nhlrank
PROJECT_HOME_DIR ?= ~/.$(PROJECT_PKG_NAME)
#PROJECT_HOME_DIR ?= ~/.{{cookiecutter.project_slug}}

.PHONY: install
install:	## Copy sqlite file into ${PROJECT_HOME_DIR}
	mkdir -p ${PROJECT_HOME_DIR}
	# TODO: does this respect if the file exists already?
	cp -p sql/db.sqlite3 ${PROJECT_HOME_DIR}
