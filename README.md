# gendiff - compare two configuration files
### Hexlet tests and linter status:
[![Actions Status](https://github.com/aigarzs/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aigarzs/python-project-50/actions)
![Python CI workflow](https://github.com/aigarzs/python-project-50/actions/workflows/python_ci.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/97015e3e7bc8423ec52b/maintainability)](https://codeclimate.com/github/aigarzs/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/97015e3e7bc8423ec52b/test_coverage)](https://codeclimate.com/github/aigarzs/python-project-50/test_coverage)

This program compares two JSON or YML configuration files 
and outputs differences in various formats.

## Links

This project was built using these tools:

| Tool                                           | Description                                           |
|------------------------------------------------|-------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)           | Python dependency management and packaging made easy. |
| [flake8](https://flake8.pycqa.org/en/latest/)  | Your Tool For Style Guide Enforcement.                |


## Usage

`poetry run gendiff [-h] [-f FORMAT] first_file second_file`  
  
positional arguments:  
&nbsp; &nbsp; &nbsp; first_file  
&nbsp; &nbsp; &nbsp; second_file  
  
options:  
&nbsp; &nbsp; &nbsp; -h, --help &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; show help message and exit  
&nbsp; &nbsp; &nbsp; -f FORMAT, --format FORMAT  &nbsp; &nbsp; &nbsp; set format of output  
  
If option --format omitted, default format `stylish` is applied.
Available output formats are `plain` `stylish` `json`
  
  
## Demo
[![asciicast](https://asciinema.org/a/KdAJcfbbLxFVwJ081zpw6xs17.svg)](https://asciinema.org/a/KdAJcfbbLxFVwJ081zpw6xs17)

---
## Requirements

| &nbsp; &nbsp; &nbsp; Tool &nbsp; &nbsp; &nbsp;| Description                                                                                                   |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [python 3](https://www.python.org/downloads/) | Python is a programming language that lets you work more quickly and integrate your systems more effectively. |
| [poetry](https://poetry.eustace.io/)          | Python dependency management and packaging made easy.                                                         |


---
## Install
```
git clone https://github.com/aigarzs/python-project-50
cd python-project-50
pip install poetry
make install
```

