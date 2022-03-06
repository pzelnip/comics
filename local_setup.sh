#!/bin/sh


# deprecated, if you want to go back to postgresql, these are the rough steps
# createdb comics
# createuser comics
# psql -c "GRANT CONNECT ON DATABASE comics TO comics;"
# psql -c "ALTER USER comics PASSWORD 'comics';"

touch comics.sqlite3
export DJANGO_SETTINGS_MODULE=comics.settings.local
python manage.py migrate
