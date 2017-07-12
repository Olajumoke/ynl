# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CostSetting(models.Model):
    """ The stakeholders cost in percentage """
    amount   = models.IntegerField()
    
    
    def __unicode__(self):
        return '%s' %(self.amount)