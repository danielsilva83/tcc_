
web: gunicorn myproject.wsgi  --bind 0.0.0.0:$PORT --worker-class gthread --threads 8 --timeout 800
web: python install --upgrade pip
web: python manage.py runserver 0.0.0.0:\$PORT
