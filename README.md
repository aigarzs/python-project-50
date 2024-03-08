### Hexlet tests and linter status:
[![Actions Status](https://github.com/aigarzs/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aigarzs/python-project-50/actions)
![Python CI workflow](https://github.com/aigarzs/python-project-50/actions/workflows/python_ci.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/97015e3e7bc8423ec52b/maintainability)](https://codeclimate.com/github/aigarzs/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/97015e3e7bc8423ec52b/test_coverage)](https://codeclimate.com/github/aigarzs/python-project-50/test_coverage)

## Links

This project was built using these tools:

| Tool                                           | Description                                             |
|------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)           | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/en/latest/)  | "Your Tool For Style Guide Enforcement"                 |

---
## Install
```
git clone https://github.com/aigarzs/python-project-50
cd python-project-50
pip install poetry
make install
```

## Usage
This program compares two JSON or YML files and outputs differences in FORMAT.
If option --format omitted, default format `stylish` is applied.
Available output formats are `plain` `stylish` `json`

`poetry run gendiff --format FORMAT file1_path file2_path`


## Demo
[![asciicast](https://asciinema.org/a/KdAJcfbbLxFVwJ081zpw6xs17.svg)](https://asciinema.org/a/KdAJcfbbLxFVwJ081zpw6xs17)
