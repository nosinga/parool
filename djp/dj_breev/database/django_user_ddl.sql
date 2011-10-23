create or replace view django_user_vw
as
select usr.id as id
,      usr.username as username
,      prf.vaadin_password as password
from   auth_user usr
,      breev_userprofile prf
where  usr.id = prf.user_id
;

create or replace view users_vw
as
select usr.id as id
,      usr.username as username
from   auth_user usr
,      breev_userprofile prf
where  usr.id = prf.user_id
;

create or replace 
function menu_hasdjangouserleafchild 
         ( p_menu_id      in integer
         , p_username     in varchar
         , p_menuleaftype in varchar)
    returns integer as $$
    
  declare l_menu_id integer;
  declare l_username varchar;
  declare l_menuleaftype varchar;  
  declare l_return integer default 0;
    
  declare
    csr_childmenu cursor
    is
      select id
        from urp_menunodes
       where parent_id = l_menu_id;

  declare
    csr_menuleaf cursor
    is
      select id
        from urp_menuleaf_vw
       where menu_id = l_menu_id and menuleaftype = coalesce (l_menuleaftype, menuleaftype)
       and   id in (
                    select pms.id
                    from   django_user_vw      usr
                    ,      urp_permissions     pms
                    ,      urp_role_permission rpm
                    ,      urp_user_role       url
                    where  usr.id = url.usr_id
                    and    pms.id = rpm.pms_id
                    and    rpm.rle_id = url.rle_id
                    and    usr.username = l_username
                   )
                   ;
  begin  
    l_menu_id      = p_menu_id;
    l_username     = p_username;
    l_menuleaftype = p_menuleaftype;

    for r_menuleaf in csr_menuleaf
    loop
      l_return := 1;
      exit;
    end loop;
    if l_return = 0
    then
      for r_childmenu in csr_childmenu
      loop
        l_return :=  menu_hasdjangouserleafchild (r_childmenu.id, p_username, p_menuleaftype);
        if l_return = 1
        then
          exit;
        end if;
      end loop;
    end if;
    return l_return;
  end;
$$ LANGUAGE plpgsql;

