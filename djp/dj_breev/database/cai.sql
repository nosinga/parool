-- each object is dropped individually from now
-- drop owned by auk; -- auk is example of role name in postgres

set client_min_messages='warning'
;

\echo drop breev tables
\i breev_drop.sql

\echo drop django and auth tables
\i django_drop.sql

\echo create django tables part 1
\i django_generated1.sql

\echo create auth tables 
\i auth_generated.sql

\echo create django tables part 2
\i django_generated2.sql

\echo create breev tables
\i breev_generated.sql

\echo django_user_ddl.sql
\i django_user_ddl.sql

\echo django_data.sql
\i django_data.sql

\echo django_breev_data.sql
\i django_breev_data.sql

\echo django_bot_ddl.sql
\i django_bot_ddl.sql

\echo django_bot_data.sql
\i django_bot_data.sql

set client_min_messages='notice'
;
