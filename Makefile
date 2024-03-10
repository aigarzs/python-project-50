lint:
	poetry run flake8 scripts gendiff tests 

install:
	poetry install

check:
	poetry run flake8 scripts gendiff tests
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=gendiff

