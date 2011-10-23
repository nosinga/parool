from django.conf import settings
from django.db import connection, transaction
from django.db.utils        import DatabaseError

import re
import ConfigParser
#
# De queries die gebruikt worden 
# worden uit een aparte file gehaald
# hiervoor worden onderstaande 
# hulp functie gebruikt
#
# Daar het alleen gaat om queries en 
# niet updates en data definitie veranderingen
# spreken we over sqldql (sql data query language)
# dml (data manipulation language) en
# ddl (data definitiion language)
# blijven hiet nog buiten beschouwing
#
def get_sql(section,statementname) :
  cp = ConfigParser.ConfigParser()
  cp.read(settings.PROJECT_DIR + "/sqldql/sqldql.sql")
  sqldql = cp.get(section,statementname)
  # als in file bindvariables staan dan worden ze vervangen door %s
  sqldql = re.sub(r':([^\s]+)','%s',sqldql)
  return sqldql

def get_sqlrecordset(section,statementname,variables) :
  sqldql = get_sql(section,statementname)
  conn_cursor   = connection.cursor()
  # variables worden meegegeven als tuple of list aan onderstaande call
  conn_cursor.execute(sqldql,variables)
  return conn_cursor.fetchall()
#
# onderstaande functie wordt gebruikt om de records 
# uit recordset van een tuple '()'
# om te schrijven naar een directorie '{}'
# hierdoor kunnen in een template de record waardes
# eenvoudig met een key:value constructie opgehaald worden
# hiermee blijft de template heel leesbaar
#
# TODO beschrijf django queryset
# versus
# django rawrecordset
# versus
# import psycopg2.extras
# conn = psycopg2.connect("dbname=" + db_name + " user=" + db_username + " password=" + db_password)
# conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#
def recordset2recordset_with_columnnames(recordset,cursor_description) :
  columnnames = []
  for column in cursor_description :
    columnnames.append(column[0])

  recordset_with_columnnames = []
  for record in recordset :
    recordlist = zip(columnnames,record)
    print recordlist
    recorddict = dict(recordlist)
#    print recorddict
    recordset_with_columnnames.append(recorddict)

  return columnnames, recordset_with_columnnames
#
# 
def get_sqlrecordset_with_columnnames(sqlstatement,bindvariables) :
  cursor   = connection.cursor()
  variables = []
  # ugly hack om postgresql casting in rapporten toe te staan, part 1 
  sqlstatement = sqlstatement.replace("::","####")
  sqlvariables = re.findall(r':([^\s]+)',sqlstatement)
  if sqlvariables :
     sqlstatement = re.sub(r':([^\s]+)','%s',sqlstatement)
     #  shortcut if things don't work
     #sqlstatement = sqlstatement.replace(":","")
     for sqlvariable in sqlvariables :
         variable = bindvariables[sqlvariable]
         variables.append(variable)
  
  if type(bindvariables) is list :
     variables = bindvariables       

  # ugly hack om postgresql casting in rapporten toe te staan, part 2 
  sqlstatement = sqlstatement.replace("####","::")
  try :
    cursor.execute(sqlstatement,variables)
  except DatabaseError, extraInfo :
    cursor.execute('rollback')
    raise DatabaseError, extraInfo

  colnames, recordset_with_columnnames = (
    recordset2recordset_with_columnnames(cursor.fetchall(),cursor.description))
  return colnames, recordset_with_columnnames
