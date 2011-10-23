import psycopg2
import ConfigParser

import vktrouw_search
reload(vktrouw_search)

##
## initialistaie
##
# open connectie
cp = ConfigParser.ConfigParser()
cp.read("db.properties")
db_name     = cp.get('database','db_name')
db_username = cp.get('database','db_username')
db_password = cp.get('database','db_password')
conn = psycopg2.connect("dbname=" + db_name + " user=" + db_username + " password=" + db_password)
# open cursor om artikelen en categorieen op te halen
categorie_cur  = conn.cursor()

# maak en execute statement om categorieen te selecteren
categorie_cur.execute("select id, cloud from auk_categorie order by 2,1")
i = 0
# loop over de categorieen heen
for categorie in categorie_cur:
  i = i + 1

  # initialiseer searcher class
  e=vktrouw_search.searcher()
  
  print categorie[1].lower()
  cloud_words = categorie[1].lower().split()
  
  for word in cloud_words :
   
    rankedscores = e.modquery(word)
    for (score,artikelid) in rankedscores[0:100]:             
       print '%f\t%s' % (score,artikelid)
    
       artikel_categorie_exists_cur = conn.cursor()
       artikel_categorie_exists_cur.execute("select id from auk_artikel_categorie where art_id = %s and cat_id = %s " , (artikelid,categorie[0])) 
       artikel_categorie_exists = artikel_categorie_exists_cur.fetchone()
       if artikel_categorie_exists == None :
         artikel_categorie_cur = conn.cursor()
         artikel_categorie_cur.execute("""insert into auk_artikel_categorie 
                                        (art_id, cat_id, cloud_weight)
                                        values
                                        (%s, %s, %s)""",
                                        (artikelid,categorie[0],score)
                                      )
       else :
         artikel_categorie_cur = conn.cursor()
         artikel_categorie_cur.execute("""update auk_artikel_categorie
                                          set cloud_weight = coalesce(cloud_weight,0) + %s
                                          where art_id = %s
                                          and   cat_id = %s 
                                          """,
                                        (score,artikelid,categorie[0])
                                      )

conn.commit();
    
