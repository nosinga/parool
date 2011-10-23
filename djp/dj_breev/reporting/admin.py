from django.contrib import admin
from reporting.models import *

#class UserProfileAdmin(admin.ModelAdmin):
#  pass

    
class ReportAdmin(admin.ModelAdmin):
  list_display=('name',)
  list_filter=('name',)
  ordering=('name',)
  search_fields = ('name',)


admin.site.register(Report, ReportAdmin)

