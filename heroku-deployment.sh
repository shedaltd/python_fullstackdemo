# Login: first time when you deploy it
# heroku login
# heroku git:remote -a shedafullstackdemo # connect the project with the repo

cd backend
source env/bin/activate
rm -rf .tox
tox

# python manage.py collectstatic --noinput # first time to deployment

cd ..
heroku config:set DJANGO_SETTINGS_MODULE=todo.settings.prod
git subtree push --prefix backend heroku master
heroku run python manage.py migrate

# heroku run ./create.sh # run it if deploy for the first time