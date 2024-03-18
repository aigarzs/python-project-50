lint:
	poetry run flake8 gendiff tests 

install:
	poetry install

check:
	poetry run flake8 gendiff tests
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov-report xml --cov=gendiff

