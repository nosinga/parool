import re

from django.core.management import setup_environ

import settings
setup_environ(settings)

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils        import IntegrityError

from django.db import transaction

from breev.models import *

def delete_wordandwordlist():
  del_cur = connection.cursor()
  del_cur.execute("delete from sar_wordlist")
  del_cur.execute("delete from sar_wordlocation")
  del_cur.close()

# indexeer de woorden van een artikel
@transaction.commit_manually
def indexwords(artikel,ignorewords):

  # haal de individuele woorden eruit
  words = getwords(artikel.titel + ' ' + artikel.body_clean)
  for location in range(len(words)):         
     word=words[location]                       
     # kijk of woord in ignore words zit
     if word in ignorewords: continue     
     # kijk of woord al in woord entry zit en haal id op
     
     try :
        SarWordlist.objects.get(word = word)
     except ObjectDoesNotExist :   
        # save word
        sarword, created = SarWordlist.objects.get_or_create(
                word              = word
             )
           
     sarword = SarWordlist.objects.get(word = word)
     
     # maak een connectie tussen word en artikel
     sarwordlocation = SarWordlocation(
                  art      =  artikel
                , wrd      =  sarword
                , location =  location)
     
     try :           
       sarwordlocation.save()           
     except IntegrityError :
       transaction.rollback()
     else :
       transaction.commit() 

def getwords(txt):
  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)
  # Convert to lowercase
  return [word.lower() for word in words if word!='']


def main() :
  artikels = AukArtikel.objects.all().iterator()
  # Create a list of words to ignore
  ignorewordlist = [ ignoreword.word for ignoreword in SarIgnorewordlist.objects.all() ]

  i = 0
  # loop over de artikelen heen
  for artikel in artikels:
      i = i + 1
      print i
      if SarWordlocation.objects.filter(art=artikel): continue

      indexwords(artikel,ignorewordlist)
  artikels = None
