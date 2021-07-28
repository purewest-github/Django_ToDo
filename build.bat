@echo off

rem データベースを作成する
docker-compose run web python3 manage.py migrate
rem イメージの構築、コンテナの構築・起動
docker-compose up --build

exit 0