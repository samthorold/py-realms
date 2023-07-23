lint:
	poetry run black py_realms tests --preview
	poetry run flake8 py_realms tests

type-check:
	poetry run mypy py_realms tests

type-check-watch:
	find py_realms tests -name "*.py" | entr poetry run mypy py_realms tests

check: lint type-check

ci-test:
	poetry run coverage run -m pytest
	poetry run coverage report -m --skip-covered

test-watch:
	find py_realms tests -name "*.py" | entr poetry run pytest

test: check ci-test

build-docs:
	poetry run mkdocs build
