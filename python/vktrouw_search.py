import psycopg2
import ConfigParser

##
## initialistaie
##
# definieer db credentials connectie
cp = ConfigParser.ConfigParser()
cp.read("db.properties")
db_name     = cp.get('database','db_name')
db_username = cp.get('database','db_username')
db_password = cp.get('database','db_password')


class searcher:
  def __init__(self):
    self.con=psycopg2.connect("dbname=" + db_name + " user=" + db_username + " password=" + db_password)

  def __del__(self):
    self.con.close()

  def getmatchrows(self,q):
    # Strings to build the query
    fieldlist='w0.art_id'
    tablelist=''  
    clauselist=''
    wordids=[]
    rows=[]

    # Split the words by spaces
    words=q.split(' ')  
    tablenumber=0

    for word in words:
      # Get the word ID
      
      wordrow_cur=self.con.cursor()
      wordrow_cur.execute("select id from sar_wordlist where word= %s ", (word,)) 
      wordrow = wordrow_cur.fetchone()     
      if wordrow!=None:
        wordid=wordrow[0]
        wordids.append(wordid)
        if tablenumber>0:
          tablelist+=','
          clauselist+=' and '
          clauselist+='w%d.art_id=w%d.art_id and ' % (tablenumber-1,tablenumber)
        fieldlist+=',w%d.location' % tablenumber
        tablelist+='sar_wordlocation w%d' % tablenumber      
        clauselist+='w%d.wrd_id=%d' % (tablenumber,wordid)
        tablenumber+=1

        # Create the query from the separate parts
        fullquery='select %s from %s where %s' % (fieldlist,tablelist,clauselist)
#        print fullquery
        cur = self.con.cursor()
        cur.execute(fullquery)
        rows=[row for row in cur]

    return rows,wordids
    
  def getscoredlist(self,rows,wordids):
    totalscores=dict([(row[0],0) for row in rows])

    weights = []  
 
    if rows :
      # This is where we'll put our scoring functions
      weights = [(1.0,self.locationscore(rows))
                ,(1.0,self.frequencyscore(rows))
                ,(1.0,self.distancescore(rows))
                ]

    for (weight,scores) in weights:
      for artikel in totalscores:
        totalscores[artikel]+=weight*scores[artikel]

    return totalscores

  def getartikelname(self,id):
    artikel_cur = self.con.cursor()
    artikel_cur.execute ("select titel from auk_artikel where id=%s ", (id,))
    artikel = artikel_cur.fetchone()
    return artikel[0]
    
  def query(self,q):
    rows,wordids=self.getmatchrows(q)
    scores=self.getscoredlist(rows,wordids)
    rankedscores=[(score,artikel) for (artikel,score) in scores.items()]
    rankedscores.sort()
    rankedscores.reverse()
    for (score,artikelid) in rankedscores[0:1000]:
      print '%f\t%s' % (score,self.getartikelname(artikelid))
#    return wordids,[r[1] for r in rankedscores[0:10]]

  def modquery(self,q):
    rows,wordids=self.getmatchrows(q)
    scores=self.getscoredlist(rows,wordids)
    rankedscores=[(score,artikel) for (artikel,score) in scores.items()]
    rankedscores.sort()
    rankedscores.reverse()
    return rankedscores

  def normalizescores(self,scores,smallIsBetter=0):                                   
    vsmall=0.00001 # Avoid division by zero errors                                
    if smallIsBetter:                                                             
      minscore=min(scores.values())                                               
      return dict([(u,float(minscore)/max(vsmall,l)) for (u,l) in scores.items()])
    else:                                                                         
      maxscore=max(scores.values())                                               
      if maxscore==0: maxscore=vsmall                                             
      return dict([(u,float(c)/maxscore) for (u,c) in scores.items()])            

  def frequencyscore(self,rows):                                                                                                                     
    counts=dict([(row[0],0) for row in rows])                      
    for row in rows: counts[row[0]]+=1                             
    return self.normalizescores(counts)                            
                                                                   
  def locationscore(self,rows):                                    
    locations=dict([(row[0],1000000) for row in rows])             
    for row in rows:                                               
      loc=sum(row[1:])                                             
      if loc<locations[row[0]]: locations[row[0]]=loc              
                                                                   
    return self.normalizescores(locations,smallIsBetter=1)         
                                                                   
  def distancescore(self,rows):                                    
    # If there's only one word, everyone wins!                     
    if len(rows[0])<=2: return dict([(row[0],1.0) for row in rows])
                                                                   
    # Initialize the dictionary with large values                  
    mindistance=dict([(row[0],1000000) for row in rows])           
                                                                   
    for row in rows:                                               
      dist=sum([abs(row[i]-row[i-1]) for i in range(2,len(row))])  
      if dist<mindistance[row[0]]: mindistance[row[0]]=dist        
    return self.normalizescores(mindistance,smallIsBetter=1) 
