from django.core.management import setup_environ

import settings
setup_environ(settings)


from djangobot.models import *

def endlessloop() :
  while True :
    Task.run_all()

if __name__=='__main__':
    Task.run_all()
