#!/usr/bin/bash

docker-compose run web python3 manage.py migrate
docker-compose up --build