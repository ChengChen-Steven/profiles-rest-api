print("Hello World!")



## Initiate Vagrant (create Vagrantfile)
## - type of server: ubuntu/bionic64 image
## - will create a Vagrantfile in our current directory
## - Vagrantfile should include the dependency of Vagrant server
## - guest machine: dev server (Vagrant), host machine: laptop
# vagrant init ubuntu/bionic64

## Download the image we specify in Vagrantfile and use VirtualBox to create a new virtual machine
## and then run of provisioning script when starting the machine 
# vagrant up

## Connect to vagrant server
## Vagrant will handle the connection for you
# vagrant ssh

## Disconnect from vagrant server to local machine
# exit 

## Create an empty file
# touch file.txt

## Commit file to git and push to Github
# git add .
# git commit -am "Configurate Vagrant"
# git push origin


## create python virtual environment
## this won't sync with local machine
# vagrant ssh
# cd /vagrant
# python -m venv ~/env

## activate virtual environment
# source ~/env/bin/activate

## install requirements
# pip install -r requirements.txt

## deactivate virtual environment
# deactivate


## Create a django project: profiles_project
# . means putting file in root
# django-admin.py startproject profiles_project .

## Create an app: profiles_api
# python manage.py startapp profiles_api

## Enable the app in django project
## in ./profiles_project/settings.py, "INSTALLED_APPS"
## add app to this app list

## Start django dev server
# python manage.py runserver 0.0.0.0:8000

## Go to 127.0.0.1:8000, 127.0.0.1 is the local host address
## will see a port is placeheld for django
## Stop server
# ctrl-c


## Django Models
## In Django, we use models to describe data we need for application
## Django uses these models to set up and configrate our database to store our data effectively
## Each model in Django maps to a specific table within our database
## Django handles the relationship between our models and the database for us so we never need to write any sql statements or interact with the database directly

## Model
## Default user model -> for authentication
## Can be overwritten
## Best practice is to have all models in profile_apis/model.py

## Change Model - Migrations
## Everytime change or add additional model, need to change migrations file through commandline
# vagrant ssh ; cd /vagrant ; source ~/env/bin/activate
# python manage.py makemigrations profiles_api
## Run migration - make all changes required 
# python manage.py migrate

## Superuser
# vagrant ssh ; cd /vagrant ; source ~/env/bin/activate
# python manage.py createsuperuser
# email: cheng.chen.2017@marshall.usc.edu
# name: Cheng Chen
# pwd: 52Kb1314

## Enable Django admin
## profiles_api admin.py

## Test Django admin 
# python manage.py runserver 0.0.0.0:8000
## Go to 127.0.0.1:8000/admin/


## APIViews
## Give you the most control over the logic
## When to use APIViews
#### 1. Need full control over the logic
#### 2. Processing files and rendering a synchronous response
#### 3. You are calling other APIs/servies
#### 4. Accessing local files or data

## ViewSets
#### 1. A simple CRUD unterface to your database
#### 2. A quick and simple API
#### 3. Little to no customization on the logic
#### 4. Working with the standard data structures















