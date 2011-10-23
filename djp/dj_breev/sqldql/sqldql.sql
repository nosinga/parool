[main_page]
ranked_articles = 
    select *
    from   auk_artikel_rank_vw
    where  rank <= 5
    order  by cat_volgorde
    ,         rank

user_ranked_articles = 
    select *
    from auk_gebruiker_artikel_rank_vw
    where username = :sessionuser
    order by volgorde
    ,        rank

krantnaam_bij_artikel =
    select distinct krt.naam
    from   auk_krant krt
    ,      auk_rubriek rbk
    ,      auk_artikel_publicatie ap
    where  krt.id = rbk.krt_id
    and    rbk.id = ap.rbk_id
    and    ap.art_id = %s
    order by krt.naam       
         
[search_page]
search_ranked_articles =
    select *
    from   auk_artikel_rank_vw
    where  artikel_id in (select id from auk_artikel where body_clean like %s)
    or     artikel_id in (select id from auk_artikel where uniek like %s)
    order  by cat_volgorde
    ,         rank



[user_preference_page]
gebruikercategories = 
  select gc.id   id
  ,       c.id   cat_id
  ,       c.naam categorie
  ,      gc.volgorde
  ,      gc.aantal_artikelen
  from   auk_gebruiker_categorie gc
  ,      auk_categorie            c
  where  gc.cat_id = c.id
  and    gc.usr_id = %s
  order by gc.volgorde
