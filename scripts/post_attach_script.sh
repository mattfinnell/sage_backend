# Start database servers
pg_ctl start -l .out/postgres.out
sudo service redis-server start

# Install Python Dependencies
pdm install

# Make Migrations
pdm run --venv in-project python manage.py makemigrations 
pdm run --venv in-project python manage.py migrate

# Create Redis Workers
# pdm run --venv in-project python manage.py rqworker default &

pdm run --venv in-project python manage.py runserver
