# CONTRIBUTING

## Requirements

- Python 3.9
- Node 12

## Setup

```sh
poetry install
pre-commit install
yarn install
```

## Run doc server

```sh
poetry run mkdocs serve
```

## Using linter

```sh
poetry run flake8
poetry run isort . --check --diff
poetry run black . --check --diff
```

```sh
yarn run markdownlint docs
yarn run textlint docs
```
