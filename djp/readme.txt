djp staat voor django projecten (djp)

om django te draaien
1. installeer django
- download django 1.3
- python setup.py install
- django-admin.pymoet in je PATH terecht komen
2. installeer psycopg2-2.3.2
- in ieder geval kleiner dan 2.4
  want psycopg2.ProgrammingError: autocommit cannot be used inside a transaction
  deze fout treedt op mer runnen van testsuites
3. creeer een rol met rechten om een database aan te maken
- dit is nodig om testen te kunnen draaien (er wort een database test_<database> aangemaakt
   ALTER ROLE name [ [ WITH ] option [ CREATEDB] ]   
   
   $ psql -U postgres          
   Password for user postgres: 
   psql (9.0.4)                
   Type "help" for help. ;     
   
   postgres=# create role auk password 'auk' login;
   CREATE ROLE
   postgres=# create database auk owner auk encoding 'utf8';
   CREATE DATABASE
   postgres=# alter role auk with createdb;                                   ;
   ALTER ROLE
 
 
 alle regexpres in python
 http://docs.python.org/library/re.html
 
 alle field types in django
 https://docs.djangoproject.com/en/dev/ref/models/fields/
 
 authorization model
 https://docs.djangoproject.com/en/dev/topics/auth/
 
 javascript
 - firebug en console een krachtige combinatie met jQuery
 
 
Truc om boel aan de praat te krijgen op ubuntu
 zie
 http://programmingzen.com/2007/12/26/installing-django-with-postgresql-on-ubuntu/
 
 Install PostgreSQL and Psycopg2

sudo apt-get install postgresql pgadmin3 python-psycopg2

This will install PostgreSQL 8.2.5, PgAdmin III and the driver Psycopg2 for you. 
Most people at this point will ask, what’s the default password for PostgreSQL on Ubuntu? 
You can use the following instructions to set the password for the user postgres both in Ubuntu and within PostgreSQL:

sudo su -
passwd postgres
su postgres
psql template1

The last instruction should open the psql shell, where you can run the following:

ALTER USER postgres WITH ENCRYPTED PASSWORD 'mypassword';

Nu nog een probleem met
psql: FATAL:  no pg_hba.conf entry for host "172.16.186.212", user "nos"

Truc "lelijk" om dit te omzeilen
op ubuntu machine port forwarding op 5432

nos@ubuntu:~$ ssh -L 5432:localhost:5432 nanneosinga@nanne-osingas-macbook.local

Netter is om postgres server op nanne-osingas-macbook.local alle requests toe te laten
