-- each object is dropped individually from now
-- drop owned by auk; -- auk is example of role name in postgres

-- creating  djangoobjects has been turned off, they are not really changing 
-- droppping djangoobjects is not part of the scripts, if you are really sure, just remove them with by hand

set client_min_messages='warning'
;

\echo drop breev tables
\i    breev_drop.sql

-- begin django spullen die onafhankelijk van Breev zijn
-- onderstaande regels moet je aanzetten als je met
-- een volledig lege database begint
\echo create django tables
\i    django.sql
--
\echo vergroten van username veld van 30 naar 75 zodat er makkelijk een emailadres in past
\echo increase_auth_user_username_size.sql
\i    increase_auth_user_username_size.sql
--
\echo django_data.sql
\i    django_data.sql
--
\echo django_breev_data.sql
\i    django_breev_data.sql
-- einde django spullen die onafhankelijk van Breev zijn

\echo breev.sql
\i    breev.sql 

\echo drop table if exists breev_aukartikelrankvw;
      drop table if exists breev_aukartikelrankvw;

\echo breev_views.sql
\i    breev_views.sql

\echo auk_data.sql
\i    auk_data.sql
      
\echo searchandrank_data.sql
\i    searchandrank_data.sql


\echo drop_version_vaadin_objects.sql
\i    drop_version_vaadin_objects.sql
      
set client_min_messages='notice'
;
