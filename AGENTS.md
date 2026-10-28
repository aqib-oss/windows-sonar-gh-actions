# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, GitHub Copilot, etc.) working in this repository.

## Project overview

A demonstration of running SonarQube Cloud (SonarCloud) analysis on **Windows** GitHub Actions runners. The official SonarCloud GitHub Action only supports Linux runners, so this project downloads and runs the SonarScanner CLI directly on `windows-latest`. The Python package (`sonaronwindows`, a tiny `Calculator` class) exists only as sample code to analyze.

## Setup

Python 3.11+ (`pyproject.toml`: `python = ">=3.11,<4.0"`). Dependencies are managed with Poetry; CI also uses the conda environment in `environment.yml`.

```bash
poetry install                       # or: conda env create --file environment.yml && conda activate conda_sonaronwindows
pre-commit install
```

## Test and lint

```bash
poetry run pytest                    # all tests, coverage must stay >= 80%
poetry run pytest tests/sonaronwindows/test_calculator.py::test_sum
pre-commit run --all-files           # isort, black, flake8 and file hygiene hooks
```

CI (`pr-workflow.yaml`) runs `isort --check`, `black --check` and `pytest`, then the Sonar scan. Run these before opening a PR. pylint is installed but not enforced by CI or pre-commit (the existing code fails its docstring checks), so don't treat its output as required fixes.

`.pytest.ini` writes coverage to `coverage-reports\coverage.xml` (a Windows path). On macOS/Linux this creates a file literally named `coverage-reports\coverage.xml` in the repo root; it is gitignored, so leave it alone.

## Layout

- `src/sonaronwindows/` — package code
- `tests/sonaronwindows/` — tests, mirroring `src/`
- `.github/workflows/pr-workflow.yaml` — PR checks + Sonar scan
- `.github/workflows/main-workflow.yaml` — on push to `main`: tests, Sonar scan, then python-semantic-release
- `sonar-project.properties` — Sonar config (organization `aqib-oss`); Windows-style `\\` path separators are intentional

## Code conventions

- black (line length 90) and isort (black profile); flake8 with `max-line-length = 90`
- Type annotations on function parameters and return values in `src/`; annotate local variables in tests
- Tests use the Arrange / Act / Assert pattern with comments marking each section
- Workflow steps use `shell: powershell` and must work on Windows runners

## Dependencies

- When bumping black, isort or flake8, keep the `rev` in `.pre-commit-config.yaml` and the constraint in `pyproject.toml` in step.
- Update locked versions with `poetry update --lock` (`poetry lock` alone keeps existing versions in Poetry 2), and commit `poetry.lock`.
- Dependabot (`.github/dependabot.yml`) watches pip and GitHub Actions. When fixing alerts, check every entry for a package in `poetry.lock` — Poetry can lock different versions per Python version.

## Commits, branches and PRs

- Never commit to `main` directly; use a branch such as `feat/…`, `fix/…`, `chore/…`, `docs/…`.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/); python-semantic-release derives the version and `CHANGELOG.md` from them. `ci:`, `style:` and `test:` commits are excluded from the changelog. Breaking changes use `!` or a `BREAKING CHANGE:` footer.
- Do not edit the version in `pyproject.toml`, `CHANGELOG.md`, or the `X.Y.Z` release commits — the main workflow generates them.
- PR descriptions follow `.github/pull_request_template.md` ("Description of the change - What and Why" and "Testing details").
