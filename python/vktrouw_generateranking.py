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
categorie_cur  = conn.cursor()

# maak en execute statement om categorieen te selecteren
categorie_cur.execute("select id, naam from auk_categorie order by 1")
# loop over de categorieen heen
for categorie in categorie_cur:
  rank = 0
  print categorie[0]
  artikel_categorie_cur = conn.cursor()
  artikel_categorie_cur.execute("""
                                   select id 
                                   ,      coalesce(calculated_weight,0) +  coalesce(cloud_weight,0) total_weight
                                   from   auk_artikel_categorie 
                                   where cat_id = %s
                                   and    (coalesce(calculated_weight,0) +  coalesce(cloud_weight,0)) > 0
                                   order by (coalesce(calculated_weight,0) +  coalesce(cloud_weight,0)) desc
                               """ 
                               , (categorie[0],)) 
  for artikel_categorie in artikel_categorie_cur :
    rank = rank + 1
    artikel_categorie_rank_cur = conn.cursor()
    artikel_categorie_rank_cur.execute("""update auk_artikel_categorie
                                          set    total_weight = %s
                                          ,      rank         = %s
                                          where  id           = %s
                                     """,
                                   (artikel_categorie[1],rank,artikel_categorie[0])
                                 )

conn.commit();
    
