import psycopg2
import ConfigParser
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
artikel_rubriek_categorie_cur  = conn.cursor()

# maak en execute statement om artikelen en categorieen te selecteren
artikel_rubriek_categorie_cur.execute("select art_id, cat_id from auk_artikel_rubriek_categorie_vw order by 1,2")
i = 0
# loop over de artikelen en categorieen heen
for artikel_rubriek_categorie in artikel_rubriek_categorie_cur:
  i = i + 1
  print i
  print artikel_rubriek_categorie[0]
  print artikel_rubriek_categorie[1]

  artikel_categorie_exists_cur = conn.cursor()
  artikel_categorie_exists_cur.execute("select id from auk_artikel_categorie where art_id = %s and cat_id = %s " , (artikel_rubriek_categorie[0],artikel_rubriek_categorie[1])) 
  artikel_categorie_exists = artikel_categorie_exists_cur.fetchone()
  if artikel_categorie_exists == None :
    artikel_categorie_cur = conn.cursor()
    artikel_categorie_cur.execute("""insert into auk_artikel_categorie 
                                   (art_id, cat_id, krant_weight)
                                   values
                                   (%s, %s, 1)""",
                                   (artikel_rubriek_categorie[0],artikel_rubriek_categorie[1])
                                 )
  else :
    artikel_categorie_cur = conn.cursor()
    artikel_categorie_cur.execute("""update auk_artikel_categorie
                                     set krant_weight = 1
                                     where art_id = %s
                                     and   cat_id = %s 
                                     """,
                                     (artikel_rubriek_categorie[0],artikel_rubriek_categorie[1])
                                 )
conn.commit();
    
