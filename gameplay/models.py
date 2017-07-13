# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models import Event, UserAccount
from general.modelchoices import CHOICES, DECISION, GAME_STATUS
# Create your models here.



class Gameplay(models.Model):
    user        = models.ForeignKey(UserAccount, null = True, blank=True)
    event       = models.ForeignKey(Event, null=True, blank=True)
    date        = models.DateTimeField(auto_now_add=True)
    amount      = models.FloatField(max_length=15)
    choice      = models.CharField(choices=CHOICES, max_length=5,null=True,blank=True)
    status      = models.CharField(choices=GAME_STATUS, max_length=10, null=True,blank=True)
    decision    = models.CharField(choices=DECISION, max_length=10, null=True,blank=True)
    amount_won  = models.FloatField(max_length=15, default = 0.0,null=True,blank=True)
    
    
    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return unicode(self.user)