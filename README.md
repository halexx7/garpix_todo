<p align="center">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pycqa.github.io/isortE"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# TODO List GARPIX
This is a todo list was completed as part of the test task when applying for an internship at GARPIX.

<p align="center">
  <img src="https://raw.github.com/marcosvbras/todo-list-python/master/images/to-do-list.jpg" alt="Custom image"/>
</p>

## Requirements
```
python >= 3.5
click==7.1.2
Flask==1.1.4
flask-restx==0.4.0
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
jsonschema==3.2.0
MarkupSafe==2.0.1
peewee==3.14.4
pyrsistent==0.17.3
pytz==2021.1
requests==2.25.1
six==1.16.0
urllib3==1.26.5
Werkzeug==1.0.1
```

## Getting started
```bash
Заменить на свои данные
git clone https://github.com/a2975667/flask-gcp-mysql-demo.git
cd flask-gcp-mysql-demo
```

for Windows:
```
python -m venv .venv
source .venv/bin/activate
```

for UNIX like systens:
```
python3 -m venv .venv
source .venv/bin/activate
```

clone:
```
$ git clone https://github.com/greyli/todoism.git
$ cd todoism
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```

## UnitTEST


## License
MIT

-------


# TODO List in Python

[![Build Status](https://travis-ci.org/marcosvbras/todo-list-python.svg?branch=master)](https://travis-ci.org/marcosvbras/todo-list-python)

<p align="center">
  <img src="https://raw.github.com/marcosvbras/todo-list-python/master/images/to-do-list.jpg" alt="Custom image"/>
</p>

## What is this?

**TO DO List** is a simple API project created with everything that I learned on course [Do Zero ao Deploy](https://github.com/cassiobotaro/do_zero_ao_deploy) by [Cássio Botaro](https://github.com/cassiobotaro/).

This project covers the following concepts:
- Python environments with [Pipenv](https://github.com/pypa/pipenv)
- Test Driven Development with [PyTest](https://docs.pytest.org/en/latest/)
- Starting with [Flask](http://flask.pocoo.org/) framework
- Continuous Integration with [Travis](https://travis-ci.org/)
- Continuous Deployment with [Heroku](https://www.heroku.com/)

Starting from what has been taught, I improved the API with **MongoDB** persistence.

## Environment
### API
All code was written with **Python 3.6**, so, for a correct running, it is recommended to install this one.

After Python installed, it is required to install all dependencies. You can use [Pipenv](https://github.com/pypa/pipenv) or [Virtualenv](https://virtualenv.pypa.io/en/stable/). If you are using **Pipenv**, use the following command to install from **Pipfile**:

```bash
$ pipenv install
```

...and active the environment:
```bash
$ pipenv shell
```

However, if you are using **Virtualenv**, you need to activate the environment and install from **requirements.pip** file:

```bash
$ source YOUR_ENVIRONMENT_DIRECTORY/bin/activate
$ pip install -r requirements.pip
```

### Database
Install [MongoDB](https://www.mongodb.com/) in your machine and be sure **MongoDB** process is running.

## How to run

```bash
$ python todo.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

API Endpoints:
- `GET /tasks`: Return all tasks available
- `POST /tasks`: Create a new task

## Testing (Optional)

You can test the application using the development dependencies.

Install all development dependencies from **Pipfile**:
```bash
$ pipenv install --dev
```

Or from **dev-requirements.pip** file if you are using **VirtualEnv**:
```bash
$ pip install -r dev-requirements.pip
```

To debug endpoints, you can use [HTTPie](https://httpie.org/) as following:
```bash
$ http http://127.0.0.1:5000/tasks
[
  {
    "_id": {
      "$oid": "5ad3d924e3bdea6ccf9d9d3e"
    },
    "description": "The Best Description",
    "done": false,
    "title": "The Best Title"
  },
  {
    "_id": {
      "$oid": "5ad3d8fae3bdea6c41d571f4"
    },
    "description": "The Incredible Description",
    "done": false,
    "title": "The Incredible Title"
  }
]
```

```bash
$ http POST http://127.0.0.1:5000/tasks title=Test description=Test
HTTP/1.0 201 CREATED
Content-Length: 123
Content-Type: application/json
Date: Mon, 16 Apr 2018 00:23:45 GMT
Server: Werkzeug/0.14.1 Python/3.6.2

{
  "_id": {
    "$oid": "5ad3ed11e3bdea06aa7afa06"
  },
  "description": "Test",
  "done": false,
  "title": "Test"
}
```

To run the tests, you can use [PyTest](https://docs.pytest.org/en/latest/) as following:
```bash
$ python -m pytest
...
collected 7 items

test_todo.py .......                                                    [100%]
========================== 7 passed in 1.32 seconds ==========================
```
