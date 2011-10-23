from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from datetime import datetime  

##
## begin util functies
##
def nvl(value,default_value) :                    
  return default_value if value is None else value 

##
## einde util functies
##

class AukArtikelRankVw(models.Model):
    artikel_id = models.IntegerField()
    artikel_titel = models.CharField(max_length=200)
    krant = models.TextField()
    cat_id = models.IntegerField()
    cat_volgorde = models.IntegerField()
    categorie = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    pubdate_yyyymmdd = models.TextField()
    krant_weight = models.DecimalField(decimal_places=6,max_digits=10)
    calculated_weight = models.DecimalField(decimal_places=6,max_digits=10)
    cloud_weight = models.DecimalField(decimal_places=6,max_digits=10)
    total_weight = models.DecimalField(decimal_places=6,max_digits=10)
    rank = models.DecimalField(decimal_places=6,max_digits=10)
#    class Meta:
#        abstract = True

class AukArtikel(models.Model):
    uniek = models.CharField(max_length=200, unique=True)
    titel = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    rssfeeddescription = models.CharField(max_length=4000)
    url = models.CharField(max_length=1000)
    body = models.CharField(max_length=64000)
    body_clean = models.CharField(max_length=64000)
#    body_stemmed = models.CharField(max_length=64000)
    class Meta:
        db_table = u'auk_artikel'

    def __unicode__(self):
        return u'%s' % (self.uniek)

                                                                                                                                                                        
#Alles van de krant
class Krant(models.Model):
#    id = models.IntegerField(primary_key=True)
    naam = models.CharField(unique=True, max_length=100)
    url = models.CharField(max_length=1000)
    class Meta:
        db_table = u'auk_krant'

    def __unicode__(self):
        return u'%s' % (self.naam)

class Rubriek(models.Model):
    krt = models.ForeignKey(Krant)
    naam = models.CharField(max_length=100)
    url = models.CharField(unique=True,max_length=1000)
    actief = models.CharField(max_length=1)
    class Meta:
        db_table = u'auk_rubriek'

    def __unicode__(self):
        return u'%s' % (self.naam)

class Categorie(models.Model):
#    id = models.IntegerField(primary_key=True)
    volgorde = models.IntegerField()
    naam = models.CharField(unique=True,max_length=100)
    cloud = models.CharField(max_length=4000,null=True,blank=True)
    cloud_factor = models.DecimalField(default=1,max_digits=4, decimal_places=2)
    aging_factor = models.DecimalField(default=1,max_digits=4, decimal_places=2)
    class Meta:
        db_table = u'auk_categorie'

    def __unicode__(self):
        return u'%s' % (self.naam)

class GebruikerCategorie(models.Model):
#    id = models.IntegerField(primary_key=True)
    usr = models.ForeignKey(User)
    cat = models.ForeignKey(Categorie)
    volgorde = models.IntegerField()
    aantal_artikelen = models.IntegerField()
    class Meta:
        db_table = u'auk_gebruiker_categorie'
        unique_together = ("usr","cat")


#
# Intersectie tussen rubriek en categorie
#

class AukRubriekCategorie(models.Model):
    rbk = models.ForeignKey(Rubriek)
    cat = models.ForeignKey(Categorie)   
    class Meta:
        db_table = u'auk_rubriek_categorie'
        unique_together = ("rbk","cat")
                                    

#
# Intersectie tussen artikel en categorie
#

class AukArtikelCategorie(models.Model):
    art               = models.ForeignKey(AukArtikel)
    cat               = models.ForeignKey(Categorie)   
    krant_weight      = models.FloatField(null=True)
    calculated_weight = models.FloatField(null=True)
    cloud_weight      = models.FloatField(null=True)
    total_weight      = models.FloatField(null=True)
    rank              = models.IntegerField(null=True)



    class Meta:
        db_table = u'auk_artikel_categorie'
        unique_together = ("art","cat")
                                    


#
# Intersectie tussen artikel en rubriek
#

class AukArtikelPublicatie(models.Model):
    art = models.ForeignKey(AukArtikel)
    rbk = models.ForeignKey(Rubriek)
    
    class Meta:
        db_table = u'auk_artikel_publicatie'
        unique_together = ("art", "rbk")
                                    

#
# Search and Rank tabellen
#
class SarIgnorewordlist(models.Model):
    word = models.CharField(max_length=4000)
    class Meta:
        db_table = u'sar_ignorewordlist'

class SarWordlist(models.Model):
    word = models.CharField(unique=True, max_length=4000)
    class Meta:
        db_table = u'sar_wordlist'

class SarWordlocation(models.Model):
    art = models.ForeignKey(AukArtikel)
    wrd = models.ForeignKey(SarWordlist)
    location = models.IntegerField()
    class Meta:
        db_table = u'sar_wordlocation'
        unique_together = ("art", "wrd", "location")

#
#
# Logging om hierna learning te bewerkstelligen
#
class LogAction(models.Model):
     usr = models.ForeignKey(User,null=True)
     art = models.ForeignKey(AukArtikel,null=True)
     session_key       = models.CharField(max_length=40)
     first_action_time = models.DateTimeField(default=datetime.now)
     last_action_time  = models.DateTimeField()
     action            = models.CharField(max_length=100)
     spent_time        = models.IntegerField(default=0) 
     unique_together = ("usr","art","session_key")    
     
class Vote(models.Model) :     
     usr   = models.ForeignKey(User)
     art   = models.ForeignKey(AukArtikel)
     score = models.IntegerField()
     unique_together = ("usr","art")

