lint:
	poetry run black py_realms tests --preview

check:
	poetry run flake8 py_realms tests
	poetry run black py_realms tests --preview --check
	poetry run mypy py_realms tests

test: check
	poetry run coverage run -m pytest
	poetry run coverage report -m --skip-covered

