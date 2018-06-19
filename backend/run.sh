. env/bin/activate 

if [ ! -f db.sqlite3 ]; then
    python manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@local.test', 'password123')" | python manage.py shell
fi

python manage.py runserver 0.0.0.0:8000