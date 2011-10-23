from django.core.management import setup_environ

import settings
setup_environ(settings)

from exceptionformat import printExceptionInfo

from breev.models import *

def main():
  categories = Categorie.objects.all().order_by('volgorde').iterator()
  for categorie in categories :
    rank = 0
    print categorie.id, categorie.naam
    AukArtikelCategorie.objects.filter(cat=categorie).update(rank=None,total_weight=None)
    artikelcategories = AukArtikelCategorie.objects.filter(cat=categorie).iterator()
    rankedartikelcategories = []
    for artikelcategorie in artikelcategories :
      interval = (datetime.now() - artikelcategorie.art.pubdate)
      interval = float(interval.days * (3600 * 24) + interval.seconds)/(24* 3600)
      artikelcategorie.total_weight = (
           nvl(artikelcategorie.calculated_weight,0) 
        +  float(categorie.cloud_factor) * nvl(artikelcategorie.cloud_weight,0)
        -  float(categorie.aging_factor) * interval
      )
      rankedartikelcategories.append(artikelcategorie)
    
    rankedartikelcategories = sorted(rankedartikelcategories, key=lambda artikelcategorie: artikelcategorie.total_weight, reverse=True)[:50]
      
    for idx,rankedartikelcategorie in enumerate(rankedartikelcategories):
      rank = idx + 1
      try :
        print rank, rankedartikelcategorie.total_weight, rankedartikelcategorie.art.id, rankedartikelcategorie.art.uniek
      except :
        printExceptionInfo()
        continue

      articlecategorie, created = AukArtikelCategorie.objects.get_or_create(
             art=rankedartikelcategorie.art
            ,cat=rankedartikelcategorie.cat
            )
      articlecategorie.total_weight = rankedartikelcategorie.total_weight
      articlecategorie.rank = rank
      articlecategorie.save()


