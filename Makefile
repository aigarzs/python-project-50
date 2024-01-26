lint:
	poetry run flake8 hexlet_code gendiff

install:
	poetry install

check:
	poetry run flake8 hexlet_code gendiff
	poetry run pytest
