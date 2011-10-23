from django.db import models

class REPORT_DOMAIN :
    CHOICES = ( 
            ("newspaper", "newspaper"), 
            ("users","users"), 
            ("system","system"), 
    )
    SYSTEM = CHOICES[0][0]


class Report(models.Model):
    name              = models.CharField(max_length=100, unique=True)
    domain            = models.CharField(max_length=100,choices=REPORT_DOMAIN.CHOICES, default=REPORT_DOMAIN.SYSTEM)
    sqlstatement      = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=100 , blank=True, null=True)
    description       = models.CharField(max_length=4000, blank=True, null=True)
    enabled           = models.BooleanField()
    class Meta:                  
        db_table = u'rpt_report'