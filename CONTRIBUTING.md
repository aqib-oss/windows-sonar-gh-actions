# Contributing

## Table of Contents

- [Contributing](#contributing)
  - [Table of Contents](#table-of-contents)
  - [Base setup](#base-setup)

## Setup

- Install miniconda
  - Initialize conda: `conda init`
- Install Poetry
- Create the conda env: `conda env create --file environment.yml`
- Activate the conda env: `conda activate conda_sonaronwindows`
- Install the package: `poetry install`
- Install the pre-commit hooks: `pre-commit install`
- Run the pre-commit hooks on all files: `pre-commit run --all-files`
  - New, untracked files are not included in this.
