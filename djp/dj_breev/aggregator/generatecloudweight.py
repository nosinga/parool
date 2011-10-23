from django.core.management import setup_environ

import settings
setup_environ(settings)

import generate_for_search
reload(generate_for_search)

from breev.models import *

def main():

  categories = Categorie.objects.all().order_by('volgorde').iterator()
  for categorie in categories :
    # initialiseer searcher class
    e=generate_for_search.searcher()
    print categorie.cloud
    
    cloud_words = categorie.cloud.lower().split()
    
    for word in cloud_words :
      rankedscores = e.modquery(word)
      for (score,artikelid) in rankedscores[0:100]:             
         print '%f\t%s' % (score,artikelid)
         article = AukArtikel.objects.get(id=artikelid)
         articlecategorie, created = AukArtikelCategorie.objects.get_or_create(
             art=article
            ,cat=categorie
            )
         articlecategorie.cloud_weight = nvl(articlecategorie.cloud_weight,0) + score
         articlecategorie.save()

  