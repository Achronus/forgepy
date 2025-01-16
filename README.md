# forgepy

A simple CLI tool for bootstrapping new Python projects fast.

## Why It Exists

I often find myself building the same types of Python projects with the same dependencies over and over again. After a while, it gets tedious repeating the same CLI commands to create a simple project.

Forgepy combats this by using static configuration settings to build projects based on a single `create` command. There are 7 types of projects available:

1) **basic**: a simple project with [Pydantic](https://docs.pydantic.dev/latest/).
2) **api**: a [FastAPI](https://fastapi.tiangolo.com/) project with [Logfire](https://logfire.pydantic.dev/docs/).
3) **agents**: an AI Agent project with [PydanticAI](https://ai.pydantic.dev/) and [Logfire](https://logfire.pydantic.dev/docs/).
4) **dl**: a Deep Learning project with [PyTorch](https://pytorch.org/).
5) **api-agents**: a [FastAPI](https://fastapi.tiangolo.com/) and [PydanticAI](https://ai.pydantic.dev/) project (API and AGENTS).
6) **api-dl**: a Deep Learning API project (API and DL).
7) **all**: a Deep Learning, API, AI Agent project (DL and API-AGENTS).

The packages are always updated to their latest versions with every newly created project and are bootstrapped as a `Poetry` project.

## Test Packages

They also come configured with a set of test dependencies:

- [pytest](https://docs.pytest.org/en/stable/) - for unit tests.
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) - for unit test line coverage.
- [black](https://black.readthedocs.io/en/stable/) - for code formatting.
- [flake8](https://flake8.pycqa.org/en/latest/) - for confirming Python style formatting.
- [isort](https://pycqa.github.io/isort/) - for automatic import sorting.
- [mypy](https://mypy.readthedocs.io/en/stable/) - for static type checking.

## Building a Project

TBC