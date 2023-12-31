#!/bin/bash

poetry config virtualenvs.in-project true
poetry config virtualenvs.prompt ".venv"
poetry install -vv
poetry run pre-commit install
