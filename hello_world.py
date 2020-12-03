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
# cd /vagrant/
# python -m venv ~/env

## activate virtual environment
# source ~/env/bin/activate

## install requirements
# pip install -r requirements.txt

## deactivate virtual environment
# deactivate


## Create a django profiles_project
# . means putting file in root
# django-admin.py startproject profiles_project .



















