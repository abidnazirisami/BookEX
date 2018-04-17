## Version Naming convention

Progress.Member.Serial

Ex: 2.2.1 means

2 = 2nd progress showing
2 = Nitu [1 = Raida, 3 = Sami]
1 = First commit in this category

## For bangla support:

## Create database

CREATE DATABASE bookex CHARACTER SET = utf8mb4 COLLATE utf8mb4_unicode_ci;

## my.cnf

[client]
database=bookex
user=root
password=qwe123
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4

[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

# FAQ:

## Q: What to do when I can't make any changes in the database with makemigrations?
A: Let's say our app's name is appname, the model's name is modelname, mysql user is root, password is qwe123. The steps are:
	1. In your terminal,
	> mysql -u root -pqwe123
	> drop table appname_modelname;
	> delete from django_migrations where app = 'appname'
	> exit
	**Note: ** If you can't drop the table, you have to drop the whole database and migrate for all apps :(
	2. Delete the contents of appname/migrations except __init__.py
	3. Go to the django folder
	> python3 manage.py makemigrations appname
	> python3 manage.py migrate appname
