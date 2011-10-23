

drop view if exists  sar_wordcount_vw cascade;
\echo create or replace view sar_wordcount_vw
create or replace view sar_wordcount_vw
as
select wrd.word  word
,      count(1) aantal
from   auk_artikel      art
,      sar_wordlist     wrd
,      sar_wordlocation wln
where  art.id = wln.art_id
and    wrd.id = wln.wrd_id
group  by word
;

drop view if exists  auk_artikel_rubriek_categorie_vw cascade;
\echo create or replace view auk_artikel_rubriek_categorie_vw
create or replace view auk_artikel_rubriek_categorie_vw
as
select art.id                 art_id
,      art.titel              artikel
,      art.pubdate            pubdate
,      krt.id                 krt_id
,      krt.naam               krant
,      rbk.id                 rbk_id
,      rbk.naam               rubriek
,      cat.id                 cat_id
,      cat.naam               categorie
from   auk_artikel            art
,      auk_krant              krt
,      auk_rubriek            rbk
,      auk_artikel_publicatie apb
,      auk_categorie          cat
,      auk_rubriek_categorie  rct
where  art.id = apb.art_id
and    rbk.id = apb.rbk_id
and    krt.id = rbk.krt_id
and    rbk.id = rct.rbk_id
and    cat.id = rct.cat_id
;

drop view if exists  auk_artikel_rank_vw cascade;
\echo create or replace view auk_artikel_rank_vw
create or replace view auk_artikel_rank_vw
as
 select art.id                                                              id
      , art.id                                                              artikel_id
      , art.titel                                                           artikel_titel        
      , 'krant'::text                                                       krant
      , cat.id                                                              cat_id
      , cat.volgorde                                                        cat_volgorde
      , cat.naam                                                            categorie
      , art.pubdate                                                         pubdate
      , to_char(art.pubdate, 'yyyy-mm-dd hh24:mi:ss')                       pubdate_yyyymmdd
      , act.krant_weight                                                    krant_weight
      , coalesce(act.calculated_weight,    0)                               calculated_weight
      , coalesce(act.cloud_weight     ,    0)                               cloud_weight
      , coalesce(act.total_weight     ,    0)                               total_weight
      , coalesce(act.rank             , 9999)                               rank
        from  auk_artikel             art
        ,     auk_artikel_categorie   act
        ,     auk_categorie           cat
        where art.id = act.art_id
        and   cat.id = act.cat_id
;

drop view if exists  auk_gebruiker_artikel_rank_vw cascade;
\echo create or replace auk_gebruiker_artikel_rank_vw
create or replace view auk_gebruiker_artikel_rank_vw
as
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Nieuws'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Binnenland'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Buitenland'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Politiek'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Economie'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Sport'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Cultuur'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Media'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Gezondheid'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Onderwijs'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Wetenschap'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Reizen'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Groen'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Levensbeschouwing'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
union
select gct.volgorde            volgorde 
,      rnk.*     
,      usr.username            username
from   auk_artikel_rank_vw     rnk 
,      auk_gebruiker_categorie gct
,      auth_user               usr
where  rnk.categorie = 'Opinie'
and    rnk.cat_id    = gct.cat_id
and    usr.id        = gct.usr_id
and    rnk.rank     <= gct.aantal_artikelen
;
