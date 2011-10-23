from django.core.management import setup_environ

import settings
setup_environ(settings)

from django.db import connection, transaction

from breev.models import *

def main() :  

  articlepublications = AukArtikelPublicatie.objects.all().iterator()
  for articlepublication in articlepublications :
    rubriekcategories = AukRubriekCategorie.objects.filter(rbk=articlepublication.rbk).iterator()
    for rubriekcategory in rubriekcategories :
      print articlepublication.art.id , rubriekcategory.cat.id
      articlecategorie, created = AukArtikelCategorie.objects.get_or_create(
           art=articlepublication.art
          , cat=rubriekcategory.cat
          , defaults = { 'krant_weight' : 1 })
      articlecategorie.krant_weight = 1
      articlecategorie.save()
