# Django + React: A technology stack choice example for startups

- [Introduction](#Introduction)
- [Criteria](#Criteria)
- [Technology structure for web application](#Technology-structure-for-web-application)
- [One choice: Django+React](#Django-+-React)
- [Setup](#Setup)
  - [Backend Setup](#Backend-Setup)
    - [Setup Django](#Setup-Django)
    - [Set up rest framework](#Set-up-rest-framework)
    - [Set up test framework](#Set-up-test-framework)
  - [Frontend Setup](#Frontend-Setup)
    - [Basic Setup](Basic-Setup)
    - [Integrate with Django](Integrate-with-Django)
  - [Docker Setup](#Setup-Docker-to-develop)
  - [Setup deployment via heroku](Setup-deployment-via-heroku)
- [Tips](#Tips)

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
  - `mkidr backend`

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
- Setup Django settings
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
          REST_FRAMEWORK = {
            'DEFAULT_RENDERER_CLASSES': (
                'rest_framework.renderers.JSONRenderer',
            ),
            'DEFAULT_AUTHENTICATION': (
                'rest_framework.authentication.SessionAuthentication',
            ),
            'DEFAULT_PERMISSION_CLASSES': (
                'rest_framework.permissions.IsAuthenticated',
            ),
            'COERCE_DECIMAL_TO_STRING': False
        }
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
  - hint: sometimes when we run tox, it will tell us the library not installed, in fact, that is because the depencies for test need to be reinstalled. we can delete the folder .tox and run `tox` again

### Frontend Setup

  Then we setup the frontend part for the demo with react

#### Basic Setup

- Environment requirement
  - node, npm
  - install react: `npm install -g create-react-app`
  - init the react project: `create-react-app frontend`
- Config structure
  - run eject: `cd ./frontend && npm install eject`
  - it will create the config structure for us

#### Integrate with Django

- Django part
  - Install webpack loader: `pip3 install django-webpack-loader`
  - edit settings:
    ```python3
    WEBPACK_LOADER = {
      'DEFAULT': {
              'BUNDLE_DIR_NAME': 'bundles/',
              'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json'),
            }
    }
    ```
  - add template and index page
    - `cd ./backend && mkdir templates`
    - add templates settings
      ```python3
      TEMPLATES = [
          {
              # ... other settings
              'DIRS': [os.path.join(BASE_DIR, "templates"), ],
              # ... other settings
          },
      ]
      ```
    - add `index.html` in template
      ```html
      {% load render_bundle from webpack_loader %}
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width" />
          <title>Ponynote</title>
        </head>
        <body>
          <div id="root">
          </div>
            {% render_bundle 'main' %}
        </body>
      </html>
      ```
  - config `urls.py`
      ```python3
      from django.urls import path
      from django.views.generic import TemplateView
      from rest_framework import routers

      urlpatterns = [
          # ...
          path('', TemplateView.as_view(template_name="index.html"))
          # ...
      ]
      ```
  - add production setting in `backend/settings/prod.py`
    ```python3
    from base import *

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "assets"),
    ]

    WEBPACK_LOADER = {
      'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
      }
    }
    ```
  - add bundles file to allow production js setting: `mkdir -p assets/bundles`

- React part
  - install `webpack-bundle-tracker`: `npm install webpack-bundle-tracker --save-dev`
  - edit `/config/paths.js`
    ```javascript
    module.exports = {
        // ... other values
        statsRoot: resolveApp('../backend'),
      }
    ```
  - edit development configuration
    - edit `frontend/config/webpack.config.dev.js`
      - add `const publicPath = 'http://localhost:3000/';`
      - add `const publicUrl = 'http://localhost:3000/';`
      - edit module exports part:
        ```javascript
        const BundleTracker = require('webpack-bundle-tracker');
        module.exports = {
          entry: [
            // ...
            require.resolve('webpack-dev-server/client') + '?http://localhost:3000',
            require.resolve('webpack/hot/dev-server'),
          ],
          plugins: [
            new BundleTracker({path: paths.statsRoot, filename: 'webpack-stats.dev.json'}),
          ],
        }
        ```
    - edit `webpackDevServer.conf.js`
      ```javascript
      // ...
      host: host,
      headers: {
        'Access-Control-Allow-Origin': '*'
      },
      overlay: false,
      // ...
      ```
  - edit production configuration
    - edit `frontend/config/paths.js`
      ```javascript
      module.exports = {
        // ...
        appBuild: resolveApp('../assets/bundles/'),
      };
      ```
    - edit `frontend/config/webpack.config.prod.js`
      ```javascript
      const BundleTracker = require('webpack-bundle-tracker');

      const publicPath = "/static/bundles/";
      const cssFilename = 'css/[name].[contenthash:8].css';

      module.exports = {
        // ...
        output: {
          // ...
          filename: 'js/[name].[chunkhash:8].js',
          chunkFilename: 'js/[name].[chunkhash:8].chunk.js',
        },
        module: {
          // ...
          rules: [
            {
              oneOf: [
                // ...
                {
                  options: {
                    limit: 10000,
                    name: 'media/[name].[hash:8].[ext]',
                  },
                },
                {
                  // ...
                  options: {
                    name: 'media/[name].[hash:8].[ext]',
                  },
                },
              ],
            },
          ],
        },
        plugins: [
          // ...
          new BundleTracker({path: paths.statsRoot, filename: 'webpack-stats.prod.json'}),
        ],
      }
      ```
- run it
  - Dev:
    - `python manage.py runserver`
    - `yarn start`
  - Prod:
    - `yarn run build`
    - `python manage.py runserver --settings=todo.settings.prod`

### Setup Docker to develop

We we do the development, especially cooperate with others, it will be very annoying to setup the development environment.
As we can see from above, to make it work, we need to install pretty much libraries and packages, and not sure whether it will work in the end or not.
Docker can help use avoid problems like that. After we set up the docker, we only need to run `docker-compose up` and then we can start concentrate on the developing, no need to distract by environment problem.

For this application, we need 2 volumes, one is to host postgresql and store data, the other one is to store code.
We also need to set up 2 working images for Django and React.
Last but not least, we need add .dockerignore to ensure the code is clean.

We can check the docker configuration in the root directory:

- Dockerfile_django: image to host Django
- Dockerfile_react: image to host react
- docker-compose.yml: architecture
- .dockerignore: ignore no need folders and files

### Setup deployment via heroku

We want to be able to continus delivery, so the product can respond to the market feedback quickly.
Things will be pretty easy when we use heroku to deploy and host the application.

- Install heroku and login:
  - [how to install heroku](https://devcenter.heroku.com/articles/heroku-cli)
  - `heroku login`

To deploy the Django application via heroku, we will need to change backend settings

- Profile: contain the command to start the application
- runtime.txt: specify the working environment for the application
- requirements.txt: in backend direcotry and will be refered to requirements/prod.txt, heroku can only know the application is a Django application via this file.
- install gunicorn:
  - `pip install gunicorn # used to host the application`
  - config it: `web: gunicorn todo.wsgi --log-file -`
- config the static folder
  - install whitenoise: `pip install whitenoise`
  - add to settings
    ```python3
    MIDDLEWARE = [
      # ...
      'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    STATICFILES_DIRS = (
      os.path.join(BASE_DIR, 'assets'),
    )
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    ```

And then deploy it, the deployment scripts is in the repo root directory.

Our demo link is [demo](https://shedafullstackdemo.herokuapp.com/)

## Tips

1. Be careful when using the relationship database. As startup, in fact, not really know what the market wants, so we might need to change the data structure frequently. It can not be avoided, so we need to keep this in mind from the beginning of the project.
2. MongoDB could be a good choice for a early stage start up as we need to change the data structure frequently.
3. All the frontend and backend things are just a tool to make your product can be accessed by the customers. What really matters is the data behind it.
