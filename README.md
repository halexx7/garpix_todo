

# A TodoGARPIX App

<p align="left">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pycqa.github.io/isortE"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

<p align="center">
  <img src="https://raw.github.com/marcosvbras/todo-list-python/master/images/to-do-list.jpg" alt="Custom image"/>
</p>

## What is this?
This is a **TodoGARPIX** was completed as part of the test task when applying for an internship at GARPIX.

## What can?
- see the list of tasks
- create a new task
- detailed task overview
- change one task
- delete task

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

## RESTful interactions
Use Swagger UI or cUrl utility to manipulate tasks. Below is an example of using the cUrl utility:

**GET the List of todos**
```
curl -H 'Content-Type: application/json' -X 'GET' 'http://127.0.0.1:5000/api/task/'
```

**GET an individual todo**
```
curl -H 'Content-Type: application/json' -X 'GET' 'http://127.0.0.1:5000/api/task/<ID>'
```

**POST a todo**
```
curl -H 'Content-Type: application/json' -d '{"title":"Dinner", "content":"Having Dinner"}' -X 'POST' 'http://127.0.0.1:5000/api/task/'
```

**UPDATE a todo**
```
curl -H 'Content-Type: application/json' -d '{"title":"Dinner", "content":"Having Dinner"}' -X 'PUT' 'http://127.0.0.1:5000/api/task/<ID>'
```

**DELETE a todo**
```
curl -H 'Content-Type: application/json' -X 'DELETE' 'http://127.0.0.1:5000/api/task/<ID>'
```

## UnitTEST
To run the tests, you can use [unittest](https://docs.python.org/3/library/unittest.html) as following:
```bash
$ python3 -m unittest tests/test_api.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.076s

OK
```

## License
MIT




