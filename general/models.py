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
from general.modelchoices import *
from tinymce.models import HTMLField


# Create your models here.



class UserAccount(models.Model):
	""" user details """
	user            		 = models.ForeignKey(User, null=True, blank=True)
	created_on               = models.DateTimeField(auto_now_add = True)
	bank                     = models.CharField(max_length=100, null=True, blank=True)
	account_number           = models.CharField(max_length=50, null=True, blank=True)
	dob                      = models.DateField(null=True, blank=True)
	phone_number             = models.CharField(max_length=50, null=True, blank=True)
	user_image               = models.ImageField(upload_to="media/user_image/%Y/%M/%d/", null=True, blank=True)
	gender					 = models.CharField(max_length=10, null=True, blank=True, choices=GENDER)
	
	
	
	def __unicode__(self):
	    return '%s' %(self.user)

	class Meta:
		verbose_name_plural = 'UserAccount'
		ordering = ['-created_on']



class Event(models.Model):
	""" events to be created """
	author           		  = models.ForeignKey(User, null=True, blank=True)
	title                     = models.CharField(max_length=250, null=True, blank=True)
	category                  = models.CharField(max_length=50, null=True, blank=True, choices=CATEGORY)
	created_on                = models.DateTimeField(auto_now_add = True)
	start_time                = models.DateField(null=True, blank=True)
	end_time                  = models.DateField(null=True, blank=True)
	publish     			  = models.BooleanField(default=False)
	event_image               = models.ImageField(upload_to="media/event/%Y/%M/%d/", null=True, blank=True)
	admin_text                = HTMLField(null=True, blank=True)
	closed					  = models.BooleanField(default=False)
	deleted                   = models.BooleanField(default=False)
	tracking_number			  = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
	    return '%s' %(self.author)

	class Meta:
		verbose_name_plural = 'Event'
		ordering = ['-created_on']



class Comments(models.Model):
	""" comments for individual events """
	username                  = models.CharField(max_length=50, null=True, blank=True)
	text                      = models.CharField(max_length=1000, null=True, blank=True)
	created_on				  = models.DateTimeField(default=timezone.now)
	email					  = models.EmailField(blank=True, null=True)
	event 					  = models.ForeignKey('Event', null=True, blank=True)


	def __unicode__(self):
	    return '%s' %(self.username)

	class Meta:
		verbose_name_plural = 'Comment'
		ordering = ['-created_on']



# class Tags(models.Model):



