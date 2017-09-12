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
# from tinymce.models import HTMLField


# Create your models here.



class UserAccount(models.Model):
	""" user details """
	user            		 = models.ForeignKey(User, null=True, blank=True)
	created_on               = models.DateTimeField(auto_now_add = True)
	bank                     = models.CharField(max_length=100, null=True, blank=True, choices=BANK)
	account_number           = models.CharField(max_length=50, null=True, blank=True)
	dob                      = models.DateField(null=True, blank=True)
	phone_number             = models.CharField(max_length=50, null=True, blank=True)
	user_image               = models.ImageField(upload_to="media/user_image/%Y/%M/%d/", null=True, blank=True)
	gender					 = models.CharField(max_length=10, null=True, blank=True, choices=GENDER)
	deleted                  = models.BooleanField(default=False)
	
	
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
	start_time				  = models.TimeField(default=timezone.now(),auto_now_add=False)
	end_time				  = models.TimeField(default=timezone.now(),auto_now_add=False)
	start_date                = models.DateField(null=True, blank=True)
	end_date                  = models.DateField(null=True, blank=True)
	publish     			  = models.BooleanField(default=False)
	event_image               = models.ImageField(upload_to="media/event/%Y/%M/%d/", null=True, blank=True)
	event_msg_body            = models.TextField(null=True, blank=True)
	closed					  = models.BooleanField(default=False)
	deleted                   = models.BooleanField(default=False)
	event_id      			  = models.CharField(max_length=50, null=True, blank=True)
	bet_question			  = models.CharField(max_length=250, null=True, blank=True)
	event_decision			  = models.CharField(max_length=5,choices=CHOICES, null=True, blank=True)

	def __unicode__(self):
	    return '%s' %(self.author)

	class Meta:
		verbose_name_plural = 'Event'
		ordering = ['-created_on']
	
	def gameplay_total_value(self):
		return self.gameplay_set.all().aggregate(Sum('amount'))['amount__sum']
	
	def event_winnings(self):
		return self.gameplay_set.filter(choice=self.event_decision).aggregate(Sum('amount'))['amount__sum']
	
	def total_players(self):
		return self.gameplay_set.all().count()
	
	def total_amount_won(self):
		return self.gameplay_set.all().aggregate(Sum('amount_won'))['amount_won__sum']
	
	def total_winners(self):
		return self.gameplay_set.filter(choice=self.event_decision).count()

	def total_losers(self):
		return self.gameplay_set.filter(~Q(choice=self.event_decision)).count()

	def total_yes_choice(self):
		return self.gameplay_set.filter(choice="YES").count()

	def total_no_choice(self):
		return self.gameplay_set.filter(choice="NO").count()

	def get_comments(self):
		return self.comments_set.filter(deleted=False, approved=True)

	def get_comments_count(self):
		return self.get_comments().count()



class Comments(models.Model):
	""" comments for individual events """
	user                      = models.ForeignKey(User, null=True, blank=True)
	username                  = models.CharField(max_length=50, null=True, blank=True)
	text                      = models.CharField(max_length=1000, null=True, blank=True)
	created_on				  = models.DateTimeField(default=timezone.now)
	email					  = models.EmailField(blank=True, null=True)
	event 					  = models.ForeignKey(Event, null=True, blank=True)
	approved                  = models.BooleanField(default=True)
	deleted                   = models.BooleanField(default=False)
	liked                     = models.BooleanField(default=False)



	def __unicode__(self):
	    return '%s' %(self.username)

	class Meta:
		verbose_name_plural = 'Comment'
		ordering = ['-created_on']

	def get_likes(self):
		return self.likes_set.all()

	def get_likes_count(self):
		return self.get_likes().count()

	def get_all_replies(self):
		return self.replies_set.all()


class Replies(models.Model):
	""" replies to comments for individual events """
	user                = models.ForeignKey(User, null=True, blank=True)
	reply 				= models.TextField()
	comment_obj         = models.ForeignKey(Comments, null=True, blank=True)
	created_on			= models.DateTimeField(default = timezone.now)
	name                = models.CharField(max_length=150, null=True, blank=True)
	email               = models.CharField(max_length=150, null=True, blank=True)

	def __unicode__(self):
	    return '%s' %(self.username)

	class Meta:
		verbose_name_plural = 'Responses'
		ordering = ['-created_on']



class Likes(models.Model):
	""" likes to a comment"""
	user                = models.ForeignKey(User, null=True, blank=True)
	like 				= models.BooleanField(default=False)
	comment_obj         = models.ForeignKey(Comments, null=True, blank=True)
	created_on			= models.DateTimeField(default = timezone.now)
	
	def __unicode__(self):
	    return '%s' %(self.created_on)

	class Meta:
		verbose_name_plural = 'Likes'
		ordering = ['-created_on']
		



class MessageCenter(models.Model):
    user                = models.ForeignKey(User, null=True, blank=True)
    subject             = models.CharField(max_length=150, null=True, blank=True)
    created_on          = models.DateTimeField(default = timezone.now)
    message             = models.TextField()
    no_of_comments      = models.IntegerField(default=0)
    new                 = models.BooleanField(default = True)
    replied             = models.BooleanField(default=False)
    replied_on          = models.DateTimeField(null = True, blank=True)
    archive             = models.BooleanField(default=False)
    deleted             = models.BooleanField(default=False)


    class Meta:
	    verbose_name_plural = 'Messages'

    def __unicode__(self):
	    return unicode(self.user)

    def getComments(self):
		return self.messagecentercomment_set.all()

    def get_comments_count(self):
		comments_count = self.getComments().count()
		return comments_count

	



class MessageCenterComment(models.Model):
    user                    = models.ForeignKey(User, null=True, blank=True)
    message                 = models.TextField()
    date                    = models.DateTimeField(default = timezone.now)
    message_obj             = models.ForeignKey(MessageCenter, null=True, blank=True)
    image_obj               = models.ImageField(upload_to="image_obj", null=True, blank=True)


    class Meta:
	    verbose_name_plural = 'Message Center Comments'


    def __unicode__(self):
        return unicode(self.user)





