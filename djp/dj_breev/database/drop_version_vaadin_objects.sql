drop view if exists  django_user_vw         cascade;
drop view if exists  urp_menuleaf_vw        cascade;
drop view if exists  urp_menuleafnode_vw    cascade;
drop view if exists  urp_menutree_debug_vw  cascade;
drop view if exists  urp_menutree_vw        cascade;
drop view if exists  urp_user_menutree_vw   cascade;
drop view if exists  urp_user_permission_vw cascade;
drop view if exists  users_vw               cascade;

drop sequence if exists  auk_seq  cascade;
drop sequence if exists  sar_seq  cascade;
drop sequence if exists  urp_seq  cascade;


drop table if exists  ata_actions_jna  cascade;
drop table if exists  ata_logins_jna   cascade;

drop table if exists  urp_menunodes       cascade;
drop table if exists  urp_permissions     cascade;
drop table if exists  urp_role_permission cascade;
drop table if exists  urp_roles           cascade;
drop table if exists  urp_sessions        cascade;
drop table if exists  urp_sqm_connections cascade;
drop table if exists  urp_sqm_queries     cascade;
drop table if exists  urp_user_role       cascade;
drop table if exists  urp_users           cascade;

drop function if exists  menu_hasdjangouserleafchild() ;
drop function if exists  menu_hasleafchild()           ;
drop function if exists  menu_hasuserleafchild()       ;
drop function if exists  setuser()                     ;

