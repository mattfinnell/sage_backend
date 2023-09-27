sudo apt install wget ca-certificates -y
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo install postgresql postgresql-contrib psql

if [ ! -d "$PWD/.out" ]; then
    mkdir "$PWD/.out"
fi

pg_ctl start -l .out/postgres.out
psql -U postgres -f scripts/postgres.init.sql

sudo apt install redis-server -y

pdm install
pdm run --venv in-project python manage.py createsuperuser --email admin@example.com --username admin

bash scripts/generate_github_key.sh 