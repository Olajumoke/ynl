from django import template
from django.template.defaultfilters import stringfilter
from datetime import date, timedelta
from general.models import UserAccount, MessageCenter, MessageCenterComment, Event, Comments

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
	# print "val",value
	if value == 0:
		percent_value = 0
		# print value
		return percent_value
	else:
		event_total_players = Event.objects.get(pk=pk)
		percent_value = (float(value) / float(event_total_players.total_players())) * 100
		return percent_value


@register.assignment_tag
def check_user_like(request,pk):
	comment_obj = Comments.objects.get(pk=pk)
	user_obj = request.user
	likes_for_comment = comment_obj.get_likes()
	for like in likes_for_comment:
		if like.user == request.user:
			return True
		else:
			return False
			







