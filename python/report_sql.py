import psycopg2
import psycopg2.extras
import ConfigParser
import pprint

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
# open cursor om sql statement op te halen
report_cur  = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sqlstatement = """select * from urp_users"""
report_cur.execute(sqlstatement,)
#report_cur.fetchall()
rows = report_cur.fetchall()
#for row in report_cur :
pprint.pprint( report_cur.description)
#pprint.pprint( rows)
