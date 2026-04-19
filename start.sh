python -m manage migrate
gunicorn wishlist.wsgi:application --bind 0.0.0.0:8000
