-- auth
drop table if exists auth_group_permissions cascade;
\echo drop table if exists auth_group_permissions cascade;

drop table if exists auth_user_user_permissions cascade;
\echo drop table if exists auth_user_user_permissions cascade;

drop table if exists auth_user_groups cascade;
\echo drop table if exists auth_user_groups cascade;

drop table if exists auth_permission cascade;
\echo drop table if exists auth_permission cascade;

drop table if exists auth_group cascade;
\echo drop table if exists auth_group cascade;

drop table if exists auth_user cascade;
\echo drop table if exists auth_user cascade;

drop table if exists auth_message cascade;
\echo drop table if exists auth_message cascade;

-- contenttypes
drop table if exists django_content_type cascade;
\echo drop table if exists django_content_type cascade;


-- sessions
drop table if exists django_session cascade;
\echo drop table if exists django_session cascade;

-- sites
drop table if exists django_site cascade;
\echo drop table if exists django_site cascade;

-- admin
drop table if exists django_admin_log cascade;
\echo drop table if exists django_admin_log cascade;
