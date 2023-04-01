check:
	flake8 .
	black . --check
	mypy .

test: check
	pytest

