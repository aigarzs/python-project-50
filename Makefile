lint:
	poetry run flake8 hexlet_code gendiff

install:
	poetry install

check:
	poetry run flake8 hexlet_code gendiff tests
	poetry run pytest -s

test-coverage:
	poetry run pytest --cov=gendiff
