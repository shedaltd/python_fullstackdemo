. ../env/bin/activate 

python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@local.test', 'password123')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000