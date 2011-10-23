import psycopg2
conn = psycopg2.connect("dbname=auk user=auk password=auk")
titels  = conn.cursor()
titels.execute("select titel||pubdate from auk_artikel")
for titel in titels:
    print "Row: %s" % titel
    print "<<<<"
    artikel_sql = """select body_clean from auk_artikel where titel||pubdate = %s"""
    artikel = conn.cursor()
    artikel.execute(artikel_sql, titel)
    artikel_text = artikel.fetchall()
    print artikel_text
    
    artikel.close()

titels.close()
conn.close()
