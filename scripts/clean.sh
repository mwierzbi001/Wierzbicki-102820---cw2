#!/bin/bash

rm -rf .venv
rm -rf .pytest_cache
rm -rf .pylint.d
find . -type d -name "__pycache__" -exec rm -rf {} +