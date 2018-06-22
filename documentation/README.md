# Django + React: A technology stack choice example for startups

## Introduction

When you are a founder, CEO, CTO or other stakeholders for a startup company and you are in charge of developing a software product, to be specific, a web application product. The first challenge you face is to choose the proper technoloy stack for the product. A good choice can lead the product to success. However, most non-technical founders are puzzled when presented with so many technology choices for developing their ideas. And they come with a fear that committing to the wrong language or framework will have serious consequences down the road.
Today we will talk about one of the web technoloy stacks which is pretty suitable for startups.

## Criteria

So how can we decide whether the tecnholoy stack is the proper one?

From the product perspetive, we want:

- time: the product can be delivered on time
- cost: the product should be delivered within budget
- quality: the product should maintain high quality
- scope: in fact, we want to develop as many features as possible in a short time as we are startups

From the developer perspective, to acheieve the goal above, a powerful developer community will be required.

## Technology structure for web application

The modern web application is mainly divided into 2 parts:

- client side: the frontend for the application, could be a web app, mobile app or a desktop app
- server side: the backend for the application, host the application, deal with the request and data

The client side and backend side communicate via APIs.

Here are some popular technology stack.

- Frontend technology:
  - basic: html, css, javascript
  - framework: bootstrap(css), vue(js), angular(js), react(js)

- Backend technology:
  - language: javascript, python, ruby, java, .net, php
  - framework: Express(js), Django(python), Rail on ruby(ruby), Spring(java), ASP.NET(.net), Laravel(php)
  - database: MySQL, PostgreSQL, MongoDB

## Django + React

As we have said, today we will talk about the technology stack choice: Django + React

- Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It is released in 2005.
- React is a JavaScript library for building user interfaces, backed by Facebook. It is released in 2013.

The 2 framework both are open source and have powerful developer communities. There is a lot of tools and library to use. You can develop and deploy a tested high quality application quickly with them.

- Backend: Django + Django REST Framework
- Frontend:
  - React: Web app
  - React Native: Mobile app
  - Electron: Destkop app
- Database:
  - MySQL/PostgreSQL/MongoDB
- Deployment:
  - Docker to develop
  - Heroku to deploy
  - Continus Integration/Continue Delivery

With the technology stack above, you can make you application online in a day.

## Setup

- create the proejct directory
  - `mkdir shedafullstackdemo`
  - `cd ./shedafullstackdemo`
  - `mkidr backend frontend`

### Backend Setup

#### Setup Django

- environment requirement: python3, pip3
- Install virtualenv and create a virtual environment. Virtualenv is used to create a specific virtual env for the proejct. It will make it easier to manage your project.
  - `cd ./backend`
  - `pip3 install virtualenv # install package virtualenv`
  - `virtualenv --python=python3 env # create virtual environment`
  - `source env/bin/activate # activate the env`
- Install Django and Create a project
  - `pip3 install django`
  - `django-admin startproejct todo .`
- Setup the settings
  - seperate requirements for different environment into seperate files, so we can manage the requirements for different environment(dev, staging, production) more easily.
    - `mkdir requirements`
    - `pip3 freeze > requirements/base.txt`
    - `cd requirements`
    - `echo '-r base.txt' > dev.txt`
    - `echo '-r base.txt' > prod.txt`
    - `echo '-r base.txt' > test.txt`
  - seperate settings for different environment into seperate files.
    - `cd ./todo`
    - `mkdir settings && cd ./settings && touch __init__.py`
    - `mv ../settings.py base.py`
    - create the other 2 setting files for development and production: `dev.py prod.py`
    - set BASE_DIR for django project to the root directory
      - origin
        - `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
      - change to
        - `PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))`
        - `BASE_DIR = os.path.dirname(PROJECT_DIR)`
    - then later you can specifiy the setting for different environment via different file
      - to run with specific environment: `python3 manage.py runserver --settings=todo.settings.xxx`
    - run the django application and create the superuser
      - `python3 manage.py runserver`
      - `python3 manage.py createsuperuser`
      - then you can check the `http://localhost:80000`

#### Set up rest framework

  Django Rest Framework allows you to do rapid development with Django.
- Install Django Rest Framework
  - `pip3 install djangorestframework`
- Set up the settings
  1. add rest framework into `INSTALLED_APPS`
        ```python3
          INSTALLED_APPS = [
            ...
            'rest_framework',
          ]
        ```
  2. install swagger to make the APIs web browserable
  - `pip3 install django-rest-swagger`
  - add rest_framework_swagger into `INSTALLED_APPS`
      ```python3
          INSTALLED_APPS = [
            ...
            'rest_framework-swagger',
          ]
      ```
  - edit `urls.py` to make it work
    ```python3
      from django.urls import path
      from rest_framework import routers
      from rest_framework_swagger.views import get_swagger_view

      schema_view = get_swagger_view(title='Sheda Full Stack Demo')
      router = routers.DefaultRouter(trailing_slash=True)

      urlpatterns = [
          ...
          path('docs/', schema_view),
          ...
      ]
      ```
  - then run the application and check `http://localhost:8000/docs/`, you should be able to check the APIs

#### Set up test framework

  Django have the in-built test module to make the test very easy
  Except the test, we also need to control the code speficition to make sure our code clean, readable and maintainable.
  We can use `tox` altogether with `coverage`, `flake8`, `isort`, `pytest` to reach that.
- Install packages:
  - `pip3 install tox coverage flake8 isort`
- add tox, flake8, isort, coverage into `requirements/text.txt`
- create configuation files `tox.ini` and `setup.cfg` (check the backend folder)
- run the test: `tox`
  - hint:
    - sometimes when we run tox, it will tell us the library not installed, in fact, that is because the depencies for test need to be reinstalled. we can delete the folder .tox and run `tox` again

### Frontend Setup

  Then we setup the frontend part for the demo with react

- Environment requirement
  - node, npm