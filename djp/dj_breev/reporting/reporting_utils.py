from django.core.management import setup_environ

import settings
setup_environ(settings)

from reporting.models import *

import ConfigParser

class Rep :
  pass
    
def readReport(section) :
  Config = ConfigParser.ConfigParser()
  Config.read(settings.PROJECT_DIR + '/reporting/reports.ini')
  report = Rep()  
  report.id                 = section
  report.name               = Config.get(section, 'name')
  report.domain             = Config.get(section, 'domain')
  report.sqlstatement       = Config.get(section, 'sqlstatement')
  report.short_description  = Config.get(section, 'short_description')
  report.description        = Config.get(section, 'description')
  report.enabled            = Config.getboolean(section, 'enabled')
  return report

def readReports() :
  Config = ConfigParser.ConfigParser()
  Config.read(settings.PROJECT_DIR + '/reporting/reports.ini')
  sections = Config.sections()
  reports = []
  for section in sections :
    report = readReport(section)
    if report.enabled :
       reports.append(report)
  return reports

#
# run this method with the following statement
# python gen_reports_ini.py
#
def writeReports2file() :
#  reports = Report.objects.filter(enabled=True)
  reports = Report.objects.all().order_by('id')

  # create config file for next time...
  Config = ConfigParser.ConfigParser()
  cfgfile = open(settings.PROJECT_DIR + "/reporting/reports.ini",'w')
  for report in reports :

      id = str(report.id)
      # add the settings to the structure of the file, and lets write it out...
      Config.add_section(id)
      Config.set(id, 'name'             , report.name)
      Config.set(id, 'domain'           , report.domain)
      Config.set(id, 'sqlstatement'     , report.sqlstatement)
      Config.set(id, 'short_description', report.short_description)
      Config.set(id, 'description'      , report.description)
      Config.set(id, 'enabled'          , report.enabled)

  Config.write(cfgfile)
  cfgfile.close()

#
# run this method with the following statement
# python gen_reports_db.py
#
def writeReports2db() :
  reports = readReports()
  for report in reports :  
    Report.objects.get_or_create(
            name              = report.name
            , defaults = {
                'domain'            : report.domain            ,           
                'sqlstatement'      : report.sqlstatement      , 
                'short_description' : report.short_description , 
                'description'       : report.description       , 
                'enabled'           : report.enabled           , 
              }
    )
  