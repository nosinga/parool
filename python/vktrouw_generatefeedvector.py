import feedparser
import re
import psycopg2
conn = psycopg2.connect("dbname=auk user=auk password=auk")


# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(titel):
  wc={}

  # Loop over all the entries
  con = psycopg2.connect("dbname=auk user=auk password=auk")
  artikel_sql = """select body_clean from auk_artikel where titel = %s """
  artikel = con.cursor()
  artikel.execute(artikel_sql, (titel,))
  artikel_text = artikel.fetchone()
  artikel.close()
  words=getwords(artikel_text[0])
  for word in words:
      wc.setdefault(word,0)
      wc[word]+=1
  con.close()
  return titel,wc

def getwords(txt):
  # Remove all the HTML tags
#  txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
  return [word.lower() for word in words if word!='']


apcount={}
wordcounts={}
#feedlist=[line for line in file('kranten_feedlist.txt')]

titels  = conn.cursor()
titels.execute("select distinct titel from auk_artikel")
i = 0
for titel in titels:
    i = i + 1
    for titelnaam in titel:	
        try:
           title,wc=getwordcounts(titelnaam)
           print wc
           wordcounts[title]=wc
           for word,count in wc.items():
             apcount.setdefault(word,0)
             if count>1:
               apcount[word]+=1
        except:
          print 'Failed to parse feed %s' % titelnaam

wordlist=[]
for w,bc in apcount.items():
  frac=float(bc)/i
  if frac>0.1 and frac<0.5:
    wordlist.append(w)

out=file('vktrouw_kranten_data.txt','w')
out.write('Krant')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
  print blog
  out.write(blog)
  for word in wordlist:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')
