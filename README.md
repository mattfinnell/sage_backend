# Django Backend Template

This is a starting state for Django + Postgres + RedisQueue projects.

## Setup

When devcontainer is built, make sure to alter `.devcontainer.json` for the following elements...

- include the proper `"python.defaultInterpreterPath"` path which can be found via `pipenv run which python`.
- change the dev container name to the project name


## Redis

Make sure to run `pipenv run python manage.py rqworker default` to spin up a queue worker.