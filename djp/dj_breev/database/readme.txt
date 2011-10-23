Als je een herinstallatie doet op je bestaande database
- run dan het script dj_breev_reinstall.sql

Als je met een lege database begint
1. maak een user aan
   postgres=# create role auk password 'auk' login;
   CREATE ROLE
   postgres=# create database auk owner auk encoding 'utf8';
   CREATE DATABASE
   postgres=# alter role auk with createdb;                                   ;
   ALTER ROLE
 
2. de volgende regels uitcommentarieeeren ongedaan maken
   in het script dj_breev_reinstall.sql
   ( '--' voor elke regel weghalen)
  -- \echo create django tables
  -- \i    django.sql
  --
  -- \echo vergroten van username veld van 30 naar 75 zodat er makkelijk een emailadres in past
  -- \echo increase_auth_user_username_size.sql
  -- \i    increase_auth_user_username_size.sql
  -- 
  -- \echo django_data.sql
  -- \i    django_data.sql
  -- 
  -- \echo django_breev_data.sql
  -- \i    django_breev_data.sql
-- einde django spullen die onafhankelijk van Breev zijn