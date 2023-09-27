# Start database servers
pg_ctl start -l .out/postgres.out
sudo service redis-server start

# Install Python Dependencies
pipenv install

# Create Redis Workers
pipenv run python manage.py rqworker default &

# Run Django Migrations
pipenv run python manage.py makemigrations 
pipenv run python manage.py migrate