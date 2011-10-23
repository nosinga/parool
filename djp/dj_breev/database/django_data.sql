\echo insert into django_site                                                                                                                                                                                               
insert into django_site(domain, name) values 
 ( 'www.example.com' ,'www.example.com')
;

\echo insert into django_content_type
insert into django_content_type
 (name, app_label, model)
values
  ('permission','auth','permission')
 ,('group','auth','group')
 ,('user','auth','user')
 ,('message','auth','message')
 ,('content type','contenttypes','contenttype')
 ,('session','sessions','session')
 ,('site','sites','site')
 ,('log entry','admin','logentry')
;

\echo insert into auth_permission 'add'
insert into auth_permission
 (name, content_type_id, codename)
 select 'Can add '||model, id, 'add_'||model
 from django_content_type
 where app_label in ('auth'
                    ,'contenttypes'
                    ,'sessions'
                    ,'sites'
                    ,'admin')
;                    

\echo insert into auth_permission 'change'
insert into auth_permission
 (name, content_type_id, codename)
 select 'Can change '||model, id, 'change_'||model
 from django_content_type
 where app_label in ('auth'
                    ,'contenttypes'
                    ,'sessions'
                    ,'sites'
                    ,'admin')
;                    

\echo insert into auth_permission 'delete'
insert into auth_permission
 (name, content_type_id, codename)
 select 'Can delete '||model, id, 'delete_'||model
 from django_content_type
 where app_label in ('auth'
                    ,'contenttypes'
                    ,'sessions'
                    ,'sites'
                    ,'admin')
;                    

