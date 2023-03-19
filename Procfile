web: gunicorn tw_clientes.wsgi --worker-class gthread --threads 4 --timeout 120
web: gunicorn myproject.wsgi --bind 0.0.0.0:$PORT --worker-class gthread --threads 4 --timeout 120

web: python install --upgrade pip
web: python manage.py runserver 
