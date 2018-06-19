cd backend
source env/bin/activate
tox
cd ..
heroku config:set DJANGO_SETTINGS_MODULE=todo.settings.prod
git subtree push --prefix backend heroku master
heroku run python manage.py migrate
# heroku run ./run.sh # run it if deploy for the first time