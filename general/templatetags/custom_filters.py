from django import template
from django.template.defaultfilters import stringfilter
from datetime import date, timedelta
from general.models import UserAccount, MessageCenter, MessageCenterComment, Event

#from export.models import *
import datetime
import time
import pytz
from django.db.models import Q, Sum
from itertools import chain
from operator import attrgetter
from datetime import datetime  
from datetime import timedelta



register = template.Library()


@register.simple_tag
def check_last_comment_admin(request,value):
	get_match_obj = MessageCenter.objects.get(pk=value)
	all_comments = get_match_obj.getComments()
	# print all_comments
	last_comment = all_comments[len(all_comments)-1]
	if not last_comment.user.is_staff: 
		return "New Message"
	else:
		return all_comments.count()


@register.simple_tag
def check_last_comment_user(request,value):
	get_match_obj = MessageCenter.objects.get(pk=value)
	all_comments = get_match_obj.getComments()
	# print all_comments
	last_comment = all_comments[len(all_comments)-1]
	if last_comment.user.is_staff: 
		return "New Message"
	else:
		return all_comments.count()


@register.simple_tag
def getCategoryCount(value):
	category = Event.objects.filter(category=value,deleted=False)
	return category.count()


@register.simple_tag
def getPercent(value,pk):
	if value == 0:
		percent_value = 0
		print value
		return percent_value
	else:
		event_total_players = Event.objects.get(pk=pk)
		print event_total_players
		print value
		percent_value = (float(value) / float(event_total_players.total_players())) * 100
		return percent_value
	
# @register.simple_tag
# def get_comments_count(request,value):
# 	if value == 'new':
# 		get_replied_count = MessageCenter.objects.filter(user=request.user, new=True).count()
# 	elif value == 'replied':
# 		get_replied_count = MessageCenter.objects.filter(user=request.user, replied=True).count()
# 	elif value == 'archive':
# 		get_replied_count = MessageCenter.objects.filter(user=request.user, archive=True).count()
# 	else:
# 		get_replied_count = MessageCenter.objects.filter(user=request.user, deleted=True).count()
# 	return get_replied_count



# @register.simple_tag
# def get_admin_comments_count(request,value):
# 	if value == 'new':
# 		get_replied_count = MessageCenter.objects.filter(new=True).count()
# 	elif value == 'replied':
# 		get_replied_count = MessageCenter.objects.filter(replied=True).count()
# 	elif value == 'archive':
# 		get_replied_count = MessageCenter.objects.filter(archive=True).count()
# 	else:
# 		get_replied_count = MessageCenter.objects.filter(deleted=True).count()
# 	return get_replied_count






