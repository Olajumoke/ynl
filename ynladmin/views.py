# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponse , HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from wallet.models import Bank
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
from operator import attrgetter
from django.core import serializers
from django.db.models import Q
from django.contrib import messages
from django.template.context import RequestContext
from django.db.models import Count
from django import template
from itertools import chain
import re
import hashlib
import random, datetime, string
import urllib
import time
from django.core.urlresolvers import reverse
import json
from django.db.models import Sum
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from general.models import *
from general.forms import *
from general.views import paginate_list
from gameplay.models import Gameplay
# Create your views here.




def randomNumber(value):
	allowed_chars = ''.join((string.digits))
	unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))
	return '#' + value + unique_id


# @login_required
# def admin_home(request):
# 	context = {}
# 	template_name = 'ynladmin/adminHome.html'
# 	user_obj = request.user
# 	user_acc_obj = UserAccount.objects.get(user=user_obj)
# 	context['user_acc_obj'] = user_acc_obj
# 	return render(request,template_name,context)


@login_required
def admin_pages(request,pages_to):
	context = {}
	user_obj = request.user
	user_acc_obj = UserAccount.objects.get(user=user_obj)
	context['user_acc_obj'] = user_acc_obj
	if request.POST.has_key('events'):
		query = request.POST.get('search_for')
		all_events = Event.objects.filter((Q(author__username__icontains=query) |Q(title__icontains=query) |Q(category__icontains=query) |Q(publish__icontains=query) |Q(tracking_number__icontains=query)), deleted=False)
		all_event = paginate_list(request,all_events,10)
		template_name = 'ynladmin/events.html'
		event_form = EventForm()
		context['event_form'] = event_form
		context['all_events'] = all_event
	elif request.POST.has_key('users'):
		query = request.POST.get('search_for')
		template_name = 'ynladmin/users.html'
		all_user = UserAccount.objects.filter((Q(user__username__icontains=query) |Q(bank__icontains=query) |Q(dob__icontains=query) |Q(phone_number__icontains=query) |Q(gender__icontains=query) |Q(account_number__icontains=query)), deleted=False)
		all_users = paginate_list(request,all_user,10)
		useraccount_form = UserAccountForm()
		user_form = UserForm()
		context['useraccount_form'] = useraccount_form
		context['all_users'] = all_users
		context['user_form'] = user_form
	elif request.POST.has_key('messages_search'):
		template_name = 'ynladmin/messages.html'
		query = request.POST.get('search_for')
		new_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), new=True)
		replied_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), replied=True)
		archived_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), archive=True)
		deleted_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), deleted=True)
		comment_form = MessageCenterCommentForm()
		context['comment_form'] = comment_form
		context['new_messages'] = new_messages
		context['replied_messages'] = replied_messages
		context['archived_messages'] = archived_messages
		context['deleted_messages'] = deleted_messages
		context['new_count'] = new_messages.count()
		context['replied_count'] = replied_messages.count()
		context['archived_count'] = archived_messages.count()
		context['deleted_count'] = deleted_messages.count()		
	elif pages_to == 'events':
		all_event = paginate_list(request,Event.objects.filter(deleted=False),10)
		template_name = 'ynladmin/events.html'
		event_form = EventForm()
		context['event_form'] = event_form
		context['all_events'] = all_event
	elif pages_to == 'users':
		template_name = 'ynladmin/users.html'
		all_users = paginate_list(request,UserAccount.objects.filter(user__is_staff=False, deleted=False),10)
		useraccount_form = UserAccountForm()
		user_form = UserForm()
		context['useraccount_form'] = useraccount_form
		context['all_users'] = all_users
		context['user_form'] = user_form
	elif pages_to == 'messages':
		template_name = 'ynladmin/messages.html'
		rg = request.GET
		# print 'rg:',rg
		new_messages = MessageCenter.objects.filter(new=True)
		replied_messages = MessageCenter.objects.filter(replied=True)
		archived_messages = MessageCenter.objects.filter(archive=True)
		deleted_messages = MessageCenter.objects.filter(deleted=True)
		comment_form = MessageCenterCommentForm()
		context['comment_form'] = comment_form
		context['new_messages'] = new_messages
		context['replied_messages'] = replied_messages
		context['archived_messages'] = archived_messages
		context['deleted_messages'] = deleted_messages
		context['new_count'] = new_messages.count()
		context['replied_count'] = replied_messages.count()
		context['archived_count'] = archived_messages.count()
		context['deleted_count'] = deleted_messages.count()
	elif pages_to == "payment":
		template_name = 'ynladmin/payment.html'
		payments = paginate_list(request,Bank.objects.all(),10)
		context['payments'] = payments
	return render(request,template_name,context)


@login_required
def create_event(request):
	print "i got here"
	context = {}
	user_obj = request.user
	user_acc_obj = UserAccount.objects.get(user=user_obj)
	event_form = EventForm()
	all_event = paginate_list(request,Event.objects.filter(deleted=False),10)
	context['event_form'] = event_form
	context['all_events'] = all_event
	context['user_acc_obj'] = user_acc_obj
	template_name = 'ynladmin/events.html'
	if request.method == 'POST':
		rp = request.POST
		# print 'rp:', rp
		if rp.has_key('edit_event'):
			print "i wanna edit"
			event_obj = Event.objects.get(tracking_number=rp.get('event_track_num'))
			form = EventForm(request.POST, request.FILES, instance=event_obj)
			if form.is_valid:
				print 'The form is valid'
				start_date = rp.get('start_time')
				end_date = rp.get('end_time')
				if start_date >= end_date:
					messages.error(request,'Unsuccessful...Start date cannot be less than or equal to end date')
					return redirect(request.META['HTTP_REFERER'])
				else:
					print "you may proceed"
				create_event_form = form.save(commit=False)
				create_event_form.author = request.user
				create_event_form.tracking_number = rp.get('event_track_num')
				create_event_form.save()
				return redirect(reverse('ynladmin:admin_pages', args=['events']))
			else:
				print form.errors
		elif rp.has_key('edit_user'):
			print "i wanna edit this user"
			user_obj = UserAccount.objects.get(id=rp.get('user_id'))
			form = UserAccountForm(request.POST, request.FILES, instance=user_obj)
			if form.is_valid:
				print 'The form is valid'
				form.save()
				return redirect(reverse('ynladmin:admin_pages', args=['users']))
			else:
				print form.errors
		else:
			form = EventForm(request.POST, request.FILES)
			if form.is_valid:
				print 'The form is valid'
				start_date = rp.get('start_time')
				end_date = rp.get('end_time')
				if start_date >= end_date:
					messages.error(request,'Unsuccessful...Start date cannot be less than or equal to end date')
				else:
					pass
				create_event_form = form.save(commit=False)
				create_event_form.author = request.user
				create_event_form.tracking_number = randomNumber(str(rp.get('category'))[:2])
				create_event_form.save()
				return redirect(reverse('ynladmin:admin_pages', args=['events']))
			else:
				print form.errors
			return render(request,template_name,context)
		return render(request,template_name,context)
	else:
		return render(request,template_name,context)


@login_required
def delete_event(request,event_id):
	event_obj = Event.objects.get(id=event_id)
	event_obj.deleted = True
	event_obj.save()
	return redirect(reverse('ynladmin:admin_pages', args=['events']))


@login_required
def delete_user(request,user_id):
	user_obj = UserAccount.objects.get(id=user_id)
	user_obj.deleted = True
	user_obj.save()
	return redirect(reverse('ynladmin:admin_pages', args=['users']))


@login_required
def view_edit_event(request):
	context = {}
	# print request.GET
	template_name = ""
	if request.GET.has_key('edit'):
		template_name = 'ynladmin/edit_event.html'
	else:
		template_name = 'ynladmin/view_event.html'
	event_track_num = request.GET.get('event_track_num')
	event_obj = Event.objects.get(event_id=event_track_num)
	event_form = EventForm(instance=event_obj)
	context['event_track_num'] = event_track_num
	context['event_form'] = event_form
	return render(request,template_name,context)


@login_required
def edit_user(request):
	context = {}
	# print request.GET
	user_id = request.GET.get('user_id')
	useracc_obj = UserAccount.objects.get(id=user_id)
	useraccount_form = UserAccountForm(instance=useracc_obj)
	context['user_id'] = user_id
	context['useraccount_form'] = useraccount_form
	return render(request,'ynladmin/user_edit.html',context)


@login_required
def payment_filter(request, status):
	context = {}
	user_acc_obj = UserAccount.objects.get(user=request.user)
	context['user_acc_obj'] = user_acc_obj
	if status == "successful":
		template_name = 'ynladmin/payment.html'
		payments = paginate_list(request,Bank.objects.filter(status="Successful"),10)
		context['payments'] = payments
	elif status == "declined":
		template_name = 'ynladmin/payment.html'
		payments = paginate_list(request,Bank.objects.filter(status="Declined"),10)
		context['payments'] = payments
	else:
		template_name = 'ynladmin/payment.html'
		payments = paginate_list(request,Bank.objects.filter(status="Transfer"),10)
		context['payments'] = payments
	return render(request,template_name,context)



@login_required
def admin_messages(request):
	context = {}
	if request.method == 'POST':
		rp = request.POST
		# print "rp here: ", rp	
		message_obj = MessageCenter.objects.get(
			id=rp.get('msg_id')
			)
		comment_obj = MessageCenterComment.objects.create(
			message=rp.get('message'),
			message_obj=message_obj,
			image_obj=request.FILES.get('image_obj'),
			user=request.user)
		message_obj.replied = True
		message_obj.new = False
		message_obj.save()
		messages.success(request,'Message sent successfully')
		return redirect(request.META['HTTP_REFERER'])
	else:
		# print request.GET
		template_name = ""
		if request.GET.get('identifier') == 'comment':
			template_name = 'ynladmin/adminmessageComments.html'
		else:
			template_name = 'ynladmin/adminviewMessages.html'
		message_id = request.GET.get('message_id')
		message_obj = MessageCenter.objects.get(id=message_id)
		# print "msg_obj:", message_obj
		all_comments = message_obj.getComments()
		comment_form = MessageCenterCommentForm()
		context['comment_form'] = comment_form
		context['all_comments'] = all_comments
		context['message_id'] = message_id
		return render(request,template_name,context)


@login_required
def delete_message(request,pk):
	get_msg = MessageCenter.objects.get(pk=pk)
	get_msg.archive = False
	get_msg.new = False
	get_msg.deleted = True
	get_msg.replied = False
	get_msg.save()
	return redirect(request.META['HTTP_REFERER'])


@login_required
def archive_message(request,pk):
	get_msg = MessageCenter.objects.get(pk=pk)
	get_msg.archive = True
	get_msg.new = False
	get_msg.deleted = False
	get_msg.replied = False
	get_msg.save()
	return redirect(request.META['HTTP_REFERER'])
		


def close_event(request, event_id):
	event = Event.objects.get(id=event_id)
	gameplay = Gameplay.objects.filter(event=event)
	total_value = event.gameplay_total_value()
	print "Total",total_value
	return redirect(request.META['HTTP_REFERER'])












