from django.shortcuts import render_to_response,redirect
from django.template.context import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

from django.db.utils        import DatabaseError
from django.db import connection

from utils_sql import *

from reporting.models import *

from reporting.reporting_utils import *
  
@staff_member_required
def report_list(request):
     static_reports = readReports()
     flex_reports = Report.objects.filter(enabled=True)
     
     return render_to_response('reporting/reports_list.html', {'static_reports': static_reports, 'flex_reports': flex_reports},
                              context_instance=RequestContext(request))   

@staff_member_required                                                               
def view_report(request, report, output=None):

    sqlstatement = report.sqlstatement
    
    # ugly hack om postgresql casting in rapporten toe te staan, part 1 
    sqlstatement = sqlstatement.replace("::","####")

    sqlvariables = re.findall(r':([^\s]+)',sqlstatement)

    bindvariables = {}
    bindvariableslist = []
    bindvariableslist = list(set(sqlvariables))
    for variable in bindvariableslist :
      if request.POST :
         bindvariables[variable] = request.POST[variable]
      else :
         bindvariables[variable] = ""
    
    columnnames = []
    resultset = []    
    results = []
    result_headers = []
    message = ""
    if len(sqlvariables) == 0 or request.POST :

      # ugly hack om postgresql casting in rapporten toe te staan, part 2 
      sqlstatement = sqlstatement.replace("####","::")
      try :
        columnnames, resultset = get_sqlrecordset_with_columnnames(sqlstatement,bindvariables)
      except DatabaseError, extraInfo:
        message = "No valid sql statement, maybe error with null values of bindvariable : "
        message = message + str(extraInfo)
      
      if resultset :
         rows = resultset
         for row in rows :
           result = []
           for columnname in columnnames :
             columnvalue = row[columnname]
             result.append(columnvalue)
           results.append(result)
           
      else :
        if not message :
           message = "No rows returned for this report"

    return render_to_response('reporting/queryset_list.html', {'report'              : report, 
                                                               'bindvariables'       : bindvariables, 
                                                               'result_headers'      : columnnames,
                                                               'results'             : results, 
                                                               'message'             : message, 
                                                              },
                              context_instance=RequestContext(request))   

@staff_member_required                                                               
def view_static_report(request, report_id, output=None):
    report = readReport(report_id)
    return view_report(request, report)

@staff_member_required                                                               
def view_flex_report(request, report_id, output=None):
    report = Report.objects.get(pk=report_id)
    return view_report(request, report)
   

