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


