insert into auk_krant (naam,url) values ('volkskrant','http://www.volkskrant.nl');
insert into auk_krant (naam,url) values ('trouw','http://www.trouw.nl');
insert into auk_krant (naam,url) values ('nrc','http://www.nrc.nl');



-- volkskrant
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Home'                      , 'http://www.volkskrant.nl/home/rss.xml'                        ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Nieuws'                    , 'http://www.volkskrant.nl/nieuws/rss.xml'                      ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Binnenland'                , 'http://www.volkskrant.nl/nieuws/binnenland/rss.xml'           ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Buitenland'                , 'http://www.volkskrant.nl/nieuws/buitenland/rss.xml'           ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Opmerkelijk'               , 'http://www.volkskrant.nl/nieuws/opmerkelijk/rss.xml'          ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Gezondheid & wetenschap'   , 'http://www.volkskrant.nl/nieuws/gezondheidwetenschap/rss.xml' ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Media'                     , 'http://www.volkskrant.nl/nieuws/media/rss.xml'                ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Politiek'                  , 'http://www.volkskrant.nl/nieuws/politiek/rss.xml'             ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Opinie'                    , 'http://www.volkskrant.nl/opinie/rss.xml'                      ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Cultuur'                   , 'http://www.volkskrant.nl/cultuur/rss.xml'                     ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Sport'                     , 'http://www.volkskrant.nl/sport/rss.xml'                       ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Economie'                  , 'http://www.volkskrant.nl/economie/rss.xml'                    ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'volkskrant'),'Reizen'                    , 'http://www.volkskrant.nl/reizen/rss.xml'                      ,'Y');

-- trouw
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Home'                      , 'http://www.trouw.nl/home/rss.xml'                                  ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Nieuws'                    , 'http://www.trouw.nl/nieuws/rss.xml'                                ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Nederland'                 , 'http://www.trouw.nl/nieuws/nederland/rss.xml'                      ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Buitenland'                , 'http://www.trouw.nl/nieuws/buitenland/rss.xml'                     ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Politiek'                  , 'http://www.trouw.nl/nieuws/politiek/rss.xml'                       ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Economie'                  , 'http://www.trouw.nl/nieuws/economie/rss.xml'                       ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Sport'                     , 'http://www.trouw.nl/nieuws/sport/rss.xml'                          ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Cultuur'                   , 'http://www.trouw.nl/nieuws/cultuur/rss.xml'                        ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Gezondheid'                , 'http://www.trouw.nl/nieuws/gezondheid/rss.xml'                     ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Onderwijs'                 , 'http://www.trouw.nl/nieuws/onderwijs/rss.xml'                      ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Opinie'                    , 'http://www.trouw.nl/opinie/rss.xml'                                ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Groen'                     , 'http://www.trouw.nl/groen/rss.xml'                                 ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Religie-filosofie'         , 'http://www.trouw.nl/religie-filosofie/rss.xml'                     ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Schrijf'                   , 'http://www.trouw.nl/schrijf/rss.xml'                               ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Dossier: Goede Doelen'     , 'http://www.trouw.nl/goede-doelen/rss.xml'                          ,'Y');
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'trouw'),'Dossier: Moderne Manieren' , 'http://www.trouw.nl/moderne-manieren/rss.xml'                      ,'Y');

-- nrc
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'nrc'),'Binnenland'    , 'http://www.nrc.nl/nieuws/categorie/binnenland/rss.php'                           ,'Y');    
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'nrc'),'Buitenland'    , 'http://www.nrc.nl/nieuws/categorie/buitenland/rss.php'                           ,'Y');    
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'nrc'),'Economie'      , 'http://www.nrc.nl/nieuws/categorie/economie/rss.php'                             ,'Y');    
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'nrc'),'Wetenschap'    , 'http://www.nrc.nl/nieuws/categorie/wetenschap/rss.php'                           ,'Y');    
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'nrc'),'Sport'         , 'http://www.nrc.nl/nieuws/categorie/sport/rss.php'                                ,'Y');    
insert into auk_rubriek (krt_id,naam,url, actief) values ((select id from auk_krant where naam = 'nrc'),'Cultuur'       , 'http://www.nrc.nl/nieuws/categorie/cultuur/rss.php'                              ,'Y');    

\echo insert into auk_categorie                                                                                                                                                                                               
insert into auk_categorie(volgorde, naam, cloud_factor, aging_factor) values 
 ( 1 ,'Nieuws'           , 1 , 1)
,( 2 ,'Binnenland'       , 1 , 1)
,( 3 ,'Buitenland'       , 1 , 1)
,( 4 ,'Politiek'         , 1 , 1)
,( 5 ,'Economie'         , 1 , 1)
,( 6 ,'Sport'            , 1 , 1)
,( 7 ,'Cultuur'          , 1 , 1)
,( 8 ,'Media'            , 1 , 1)
,( 9 ,'Gezondheid'       , 1 , 1)
,(10 ,'Onderwijs'        , 1 , 1)
,(11 ,'Wetenschap'       , 1 , 1)
,(12 ,'Reizen'           , 1 , 1)
,(13 ,'Groen'            , 1 , 1)
,(14 ,'Levensbeschouwing', 1 , 1)
,(15 ,'Opinie'           , 1 , 1)
;

\echo insert into auk_rubriek_categorie                                                                                                                                                                                               
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Home')
                                                         ,(select id from auk_categorie where naam = 'Nieuws'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Nieuws'                   )
                                                         ,(select id from auk_categorie where naam = 'Nieuws'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Binnenland'               )
                                                         ,(select id from auk_categorie where naam = 'Binnenland'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Buitenland'               )
                                                         ,(select id from auk_categorie where naam = 'Buitenland'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Opmerkelijk'              )
                                                         ,(select id from auk_categorie where naam = 'Nieuws'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Gezondheid & wetenschap'  )
                                                         ,(select id from auk_categorie where naam = 'Gezondheid'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Gezondheid & wetenschap'  )
                                                         ,(select id from auk_categorie where naam = 'Wetenschap'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Media'                    )
                                                         ,(select id from auk_categorie where naam = 'Media'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Politiek'                 )
                                                         ,(select id from auk_categorie where naam = 'Politiek'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Opinie'                   )
                                                         ,(select id from auk_categorie where naam = 'Opinie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Cultuur'                  )
                                                         ,(select id from auk_categorie where naam = 'Cultuur'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Sport'                    )
                                                         ,(select id from auk_categorie where naam = 'Sport'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Economie'                 )
                                                         ,(select id from auk_categorie where naam = 'Economie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.volkskrant.nl/%' and naam = 'Reizen'                   )
                                                         ,(select id from auk_categorie where naam = 'Reizen'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Home'                     )
                                                         ,(select id from auk_categorie where naam = 'Nieuws'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Nieuws'                   )
                                                         ,(select id from auk_categorie where naam = 'Nieuws'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Nederland'                )
                                                         ,(select id from auk_categorie where naam = 'Binnenland'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Buitenland'               )
                                                         ,(select id from auk_categorie where naam = 'Buitenland'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Politiek'                 )
                                                         ,(select id from auk_categorie where naam = 'Politiek'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Economie'                 )
                                                         ,(select id from auk_categorie where naam = 'Economie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Sport'                    )
                                                         ,(select id from auk_categorie where naam = 'Sport'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Cultuur'                  )
                                                         ,(select id from auk_categorie where naam = 'Cultuur'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Gezondheid'               )
                                                         ,(select id from auk_categorie where naam = 'Gezondheid'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Onderwijs'                )
                                                         ,(select id from auk_categorie where naam = 'Onderwijs'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Opinie'                   )
                                                         ,(select id from auk_categorie where naam = 'Opinie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Groen'                    )
                                                         ,(select id from auk_categorie where naam = 'Groen'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Religie-filosofie'        )
                                                         ,(select id from auk_categorie where naam = 'Levensbeschouwing'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Schrijf'                  )
                                                         ,(select id from auk_categorie where naam = 'Opinie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Dossier: Goede Doelen'    )
                                                         ,(select id from auk_categorie where naam = 'Opinie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.trouw.nl/%'      and naam = 'Dossier: Moderne Manieren')
                                                         ,(select id from auk_categorie where naam = 'Opinie'));

insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.nrc%' and naam = 'Binnenland'   )   
                                                         ,(select id from auk_categorie where naam = 'Binnenland'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.nrc%' and naam = 'Buitenland'   )   
                                                         ,(select id from auk_categorie where naam = 'Buitenland'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.nrc%' and naam = 'Economie'     )   
                                                         ,(select id from auk_categorie where naam = 'Economie'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.nrc%' and naam = 'Wetenschap'   )   
                                                         ,(select id from auk_categorie where naam = 'Wetenschap'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.nrc%' and naam = 'Sport'        )   
                                                         ,(select id from auk_categorie where naam = 'Sport'));
insert into auk_rubriek_categorie (rbk_id,cat_id) values ((select id from auk_rubriek where url like 'http://www.nrc%' and naam = 'Cultuur'      )   
                                                         ,(select id from auk_categorie where naam = 'Cultuur'));

update auk_categorie 
set    cloud = ''
where  naam  = 'Nieuws' 
;
update auk_categorie 
set    cloud = 'nederland'
where naam = 'Binnenland'
;
update auk_categorie 
set    cloud = 'eu amerika asie'
where naam = 'Buitenland'
;
update auk_categorie 
set    cloud = 'pvv cda vvd pvda kamer partijen'
where naam = 'Politiek'
;
update auk_categorie 
set    cloud = 'geld financien lening hypotheek schuld rente'
where naam = 'Economie'
;
update auk_categorie 
set    cloud = 'voetbal tennis wielrennen'
where naam = 'Sport'
;
update auk_categorie 
set    cloud = 'museum muziek klassiek'
where naam = 'Cultuur'
;
update auk_categorie 
set    cloud = 'krant tv radio'
where naam = 'Media'
;
update auk_categorie 
set    cloud = 'ziek ziekenhuis kanker'
where naam = 'Gezondheid'
;
update auk_categorie 
set    cloud = 'universiteit hogeschool'
where naam = 'Onderwijs'
;
update auk_categorie 
set    cloud = 'universiteit hogeschool onderzoek'
where naam = 'Wetenschap'
;
update auk_categorie 
set    cloud = ''
where naam = 'Reizen'
;
update auk_categorie 
set    cloud = 'natuur milieu'
where naam = 'Groen'
;
update auk_categorie 
set    cloud = 'religie geloof'
where naam = 'Levensbeschouwing'
;
update auk_categorie 
set    cloud = 'mening'
where naam = 'Opinie'
;
