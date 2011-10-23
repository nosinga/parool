import urllib2
import re

from lxml import etree

from xml.etree.ElementTree import iterparse

from django.core.management import setup_environ
from django.core.exceptions import ObjectDoesNotExist

import settings
setup_environ(settings)

from breev.models import *

from exceptionformat import printExceptionInfo

def main() :
  i = 0
  aukrubrieken = Rubriek.objects.all()
  for aukrubriek in aukrubrieken :
    krant = Krant.objects.get(id=aukrubriek.krt_id)
    if aukrubriek.actief == 'Y' :
      try : 
       
       for event, elem in iterparse(urllib2.urlopen(aukrubriek.url)):
         if elem.tag == "item":
           i = i + 1
           print i
           title = elem.findtext("title")
           if title.find('#') == 0 :
             title = title[title.find(':') + 2:]
           pubdate = elem.findtext("pubDate")
           pubdate = pubdate[5:25]
            
           pubdateAsDate = datetime.strptime(pubdate, '%d %b %Y %H:%M:%S')
           pubdate = pubdateAsDate.strftime('%Y-%m-%d')
           uniek = title + "#date#" + pubdate
           
           pubdate = pubdateAsDate.strftime('%Y-%m-%d %H:%M:%S')
  
           url = elem.findtext("link")
           rssfeeddescription = elem.findtext("description")
           

           try :
             AukArtikel.objects.get(uniek = uniek)
           except ObjectDoesNotExist :   
             
             article = urllib2.urlopen(url).read()
             
             xslt_dir = settings.PROJECT_DIR + '/aggregator/xslt'
           
             # volkskrant trouw
             if krant.naam == 'volkskrant' or krant.naam == 'trouw' : 
                xslt_file = 'volkstrant_trouw.xslt'
    
             # nrc
             elif krant.naam == 'nrc' :
                xslt_file = 'nrc.xslt'
  
             xslt = xslt_dir + '/' + xslt_file
                        
             html = etree.HTML(article)
             transform = etree.XSLT(etree.XML(open(xslt).read()))
             article = transform(html)           
             
             body = str(article)
  
             # TODO dit beter maken           
             #  body_clean = re.match("<[^>]+>", body.lower())
             body_clean = body.lower()
 
           # omdat get_or_create niet werkt zoals verwacht
           # nu maar met deze try continue oplossing
           try :
             AukArtikel.objects.get(uniek = uniek)
           except ObjectDoesNotExist :   
             # save artikel
             artikel, created = AukArtikel.objects.get_or_create(
                uniek              = uniek
              , titel              = title
              , pubdate            = pubdate
              , url                = url
              , rssfeeddescription = rssfeeddescription
              , body               = body
              , body_clean         = body_clean
             )
           
           # deze regel is nodig omdat nog verkeerde sequence wordt gebruikt
           # als goede sequence wordt gebruikt is deze regel waarschijnlijk niet meer nodig
           artikel = AukArtikel.objects.get(uniek = uniek)
  
           # save artikelPublicatie
           artikelPublicatie, created = AukArtikelPublicatie.objects.get_or_create(
             art = artikel,
             rbk = aukrubriek
           )
  
         
      except :
       printExceptionInfo()
       continue
