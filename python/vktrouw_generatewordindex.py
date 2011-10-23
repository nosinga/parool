import feedparser
import re
import psycopg2
import sys
import ConfigParser

def delete_wordandwordlist():
  del_cur = conn.cursor()
  del_cur.execute("delete from sar_wordlist")
  del_cur.execute("delete from sar_wordlocation")
  del_cur.close()

# indexeer de woorden van een artikel
def indexwords(titel):
  wc={}

  # Loop over het artikel heen
  artikel_sql = """select id, titel||' '||body_clean body_clean 
                   from auk_artikel where titel = %s """
  artikel_cur = conn.cursor()
  artikel_cur.execute(artikel_sql, (titel,))
  artikel = artikel_cur.fetchone()
  artikel_cur.close()
  # haal de individuele woorden eruit
  words=getwords(artikel[1])
  for i in range(len(words)):         
     word=words[i]                       
     # kijk of woord in ignore words zit
     if word in ignorewords: continue     
     # kijk of woord al in woord entry zit en haal id op
     wordid=getwordentryid(word)
     # maak een connectie tussen word en artikel
     insertwordlocation_cur = conn.cursor()
     insertwordlocation_cur.execute("insert into sar_wordlocation(art_id,wrd_id,location) values (%s,%s,%s)", (artikel[0],wordid,i)) 


def getwords(txt):
  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)
  # Convert to lowercase
  return [word.lower() for word in words if word!='']


# Auxilliary function for getting an entry id and adding 
# it if it's not present
def getwordentryid(word):
  wordentry_cur = conn.cursor()
  wordentry_cur.execute("select id from sar_wordlist where word = %s", (word,)) 
  wordentry = wordentry_cur.fetchone()
  if wordentry == None :
    insertword_cur = conn.cursor()
    insertword_cur.execute("insert into sar_wordlist (word) values ( %s )",(word,)) 
    
    newwordentryid_cur = conn.cursor()
    newwordentryid_cur.execute("SELECT currVal('sar_seq') AS id")
    newwordentryid = newwordentryid_cur.fetchone()
    insertword_cur.close()
    newwordentryid_cur.close()
    return newwordentryid[0]
  else:
    return wordentry[0] 
  wordentry_cur.close()



def ignorewords() :
  ignorewords=[]
  ignorewords_cur = conn.cursor()
  ignorewords_cur.execute ("select word from sar_ignorewordlist")
  for ignorewords_row in ignorewords_cur :
    ignorewords.append(ignorewords_row[0])
  ignorewords_cur.close()
  return ignorewords 


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
# Create a list of words to ignore
#ignorewords={'the':1,'of':1,'to':1,'and':1,'a':1,'in':1,'is':1,'it':1}
ignorewords = ignorewords()

apcount={}
wordcounts={}
#feedlist=[line for line in file('kranten_feedlist.txt')]


delete_wordandwordlist()
# open cursor om titels op te halen
titels  = conn.cursor()

# maak en execute  statement om titels te selecteren
titels.execute("select distinct titel from auk_artikel")
##titels.execute("select titel from auk_artikel where id < (select min(id) + 3 from auk_artikel)")
i = 0
# loop over de titels heen
for titel in titels:
    i = i + 1
    for titelnaam in titel:	
#        try:
           indexwords(titelnaam)
##           print wc
##           wordcounts[title]=wc
##           for word,count in wc.items():
##             apcount.setdefault(word,0)
##             if count>1:
##               apcount[word]+=1
#        except:
#          print 'Failed to parse feed %s' % titelnaam
    conn.commit();
    
    if len(sys.argv) > 1 :
      i_exit = int(sys.argv[1])
    else :
      i_exit = 10     

    print i
    if i == i_exit :
      break

#### wordlist=[]
#### for w,bc in apcount.items():
####   frac=float(bc)/i
####   if frac>0.1 and frac<0.5:
####     wordlist.append(w)
#### 
#### out=file('vktrouw_kranten_data.txt','w')
#### out.write('Krant')
#### for word in wordlist: out.write('\t%s' % word)
#### out.write('\n')
#### for blog,wc in wordcounts.items():
####   print blog
####   out.write(blog)
####   for word in wordlist:
####     if word in wc: out.write('\t%d' % wc[word])
####     else: out.write('\t0')
####   out.write('\n')
