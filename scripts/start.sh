#!/bin/bash

ROOT_DIR="."

poetry install --all-extras
poetry run streamlit run "${ROOT_DIR}/src/agent_web_search/app/ui.py"
