from django.conf.urls.defaults import *

urlpatterns = patterns('reporting.views',
    # Listing of reports
    url('^$', 'report_list', name='reports-list'),
    url(r'^view_static/(\d+)/$', 'view_static_report', name='static-reports-view'),
    url(r'^view_flex/(\d+)/$', 'view_flex_report', name='flex-reports-view'),
)
