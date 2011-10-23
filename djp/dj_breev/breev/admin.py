from django.contrib import admin
from breev.models import *
  
class AukArtikelCategorieAdmin(admin.ModelAdmin):
  list_display=('art','cat',)

class AukArtikelPublicatieAdmin(admin.ModelAdmin):
  list_display=('art','rbk',)

class AukArtikelAdmin(admin.ModelAdmin):
  list_display=('uniek','titel',)

class AukRubriekCategorieAdmin(admin.ModelAdmin):
  list_display=('rbk','cat',)

class KrantAdmin(admin.ModelAdmin):
  list_display=('naam','url',)

class RubriekAdmin(admin.ModelAdmin):
  list_display=('krt','naam','url','actief',)

class CategorieAdmin(admin.ModelAdmin):
  list_display=('volgorde','naam','cloud','cloud_factor','aging_factor')

class GebruikerCategorieAdmin(admin.ModelAdmin):
  list_display=('usr','cat','volgorde','aantal_artikelen',)
  list_filter=('usr','cat',)
  ordering=('usr','volgorde',)

  
  
# Search and Rank
class SarIgnorewordlistAdmin(admin.ModelAdmin):
  list_display=('word',)
  ordering=('word',)  

class SarWordlistAdmin(admin.ModelAdmin):
  list_display=('word',)
  ordering=('word',)  

class SarWordlocation(admin.ModelAdmin):
  list_display=('word','art',)
#
# Logging om hierna learning te bewerkstelligen
#
class LogActionAdmin(admin.ModelAdmin):
  list_display=('usr','art')
     
class VoteAdmin(admin.ModelAdmin) :
  list_display=('usr','art')



  


admin.site.register(AukArtikelCategorie, AukArtikelCategorieAdmin)
admin.site.register(AukArtikelPublicatie, AukArtikelPublicatieAdmin)
admin.site.register(AukArtikel, AukArtikelAdmin)
admin.site.register(AukRubriekCategorie, AukRubriekCategorieAdmin)
admin.site.register(Krant, KrantAdmin)
admin.site.register(Rubriek, RubriekAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(GebruikerCategorie, GebruikerCategorieAdmin)

admin.site.register(SarIgnorewordlist,  SarIgnorewordlistAdmin)
