import os
import sys

# dit stuurt print statements naar error log ipv naar scherm
sys.stdout = sys.stderr

sys.path = ['/home/nos/workspaces/auk/djp' , '/home/nos/workspaces/auk/djp/dj_breev' , ] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'dj_breev.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

