# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from django.utils import timezone
from django.conf import settings
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.


class UserAccount(models.Model):
	user            		 = models.ForeignKey(User, null=True, blank=True)
	created_on               = models.DateTimeField(auto_now_add = True)
	bank                     = models.CharField(max_length=50, null=True, blank=True)
	account_number           = models.CharField(max_length=50, null=True, blank=True)
	dob                      = models.DateField(null=True, blank=True)
	phone_number             = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
	    return '%s' %(self.user)

	class Meta:
		verbose_name_plural = 'UserAccount'
		ordering = ['-created_on']


