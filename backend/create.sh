python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@local.test', 'password123')" | python manage.py shell