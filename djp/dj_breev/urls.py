import os
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

#admin.autodiscover()

from breev.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)


urlpatterns = patterns('',
    # Browsing
    url(r'^$', main_page),
    url(r'^article/(\d+)/$', article_page),
    url(r'^search/$',  search_page),
    url(r'^reporting/', include('reporting.urls')),
    
    # Site media    
    # in productie moet onderstaande regel uitgecommentarieerd worden
    # Apache moet de statische files serven en niet django
    # security gat
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root' : site_media}),
        
    # Session management
    url(r'^login/$', 'django.contrib.auth.views.login'),
# bovenstaande regel in verveangen door onderstaande regel
# in login page nu een voorziening getroffen om de een 
# default userprofile aan te maken als het er nog niet is
#    url(r'^login/$', login_page),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register_page),
    url(r'^register/success/$', direct_to_template,
      {'template' : 'registration/register_success.html'}),    
                                                        
    # Account Management
    url(r'^instellingen/user/(\d+)/$', user_preference_page),
    url(r'^gebruikercategoriesave/$', gebruikerCategorie_save_page),
    url(r'^vote_plus/(\d+)/$', article_vote_plus_page),
    url(r'^vote_min/(\d+)/$' , article_vote_min_page),

 
    # Examples:
    # url(r'^$', 'dj_breev.views.home', name='home'),
    # url(r'^dj_breev/', include('dj_breev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
