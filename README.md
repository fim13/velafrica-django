# Installed Apps

Django==1.9.7
django-autocomplete-light==3.1.6
django-daterange-filter==1.3.0
django-import-export==0.4.5
django-mass-edit==2.6
django-object-actions==0.8.2
django-resized==0.3.5
django-simple-history==1.8.1
django-storages==1.4.1
djangorestframework==3.3.3
Markdown==2.6.6
Pillow==3.2.0
tablib==0.11.2

# Setup

1. Install Postgres
on ubuntu: https://help.ubuntu.com/community/PostgreSQL
1.1. download and install
sudo apt-get install postgresql postgresql-contrib
ssudo apt-get install postgresql-client
1.1.1. (optional) install pgadmin
sudo apt-get install pgadmin3
1.2. create user
sudo -u postgres createuser --superuser $USER
1.3. create database
sudo -u postgres createdb $USER 


# Getting started with Django on Heroku
https://devcenter.heroku.com/articles/django-app-configuration#creating-a-new-django-project

# Database
https://devcenter.heroku.com/articles/heroku-postgresql#local-setup
DATABASE_URL: postgres://<username>:<password>@<host>/<dbname>

# Most helpful heroku toolkit cmds
`heroku login` login to heroku

`heroku config --app velafrica-admin` show all env variables

`heroku config:set ON_HEROKU=1 --app velafrica-admin` set ENV variable (necessary for choosing the right database)

`heroku pg:psql --app velafrica-admin

# Postgres command to reset currentt id
    select id from auth_group order by id DESC LIMIT 1;
     id 
    ----
     11
    alter sequence auth_group_id_seq restart with 12;

 created by Platzh1rsch (www.platzh1rsch.ch)