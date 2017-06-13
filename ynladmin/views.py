# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponse , HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict

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
	all_event = Event.objects.filter(deleted=False)
	context['all_events'] = all_event
	context['user_acc_obj'] = user_acc_obj	
	if pages_to == 'events':
		template_name = 'ynladmin/events.html'
		event_form = EventForm()
		context['event_form'] = event_form
	elif pages_to == "users":
		user_form = UserForm()
		context['user_form'] = user_form
	return render(request,template_name,context)


@login_required
def create_event(request):
	print "i got here"
	context = {}
	user_obj = request.user
	user_acc_obj = UserAccount.objects.get(user=user_obj)
	event_form = EventForm()
	all_event = Event.objects.filter(deleted=False)
	context['event_form'] = event_form
	context['all_events'] = all_event
	context['user_acc_obj'] = user_acc_obj
	template_name = 'ynladmin/events.html'
	if request.method == 'POST':
		rp = request.POST
		print 'rp:', rp
		if rp.has_key('edit_event'):
			print "i wanna edit"
			event_obj = Event.objects.get(tracking_number=rp.get('event_track_num'))
			form = EventForm(request.POST, request.FILES, instance=event_obj)
			if form.is_valid:
				print 'The form is valid'
				create_event_form = form.save(commit=False)
				create_event_form.author = request.user
				create_event_form.tracking_number = rp.get('event_track_num')
				create_event_form.save()
				return redirect(reverse('ynladmin:admin_pages', args=['events']))
			else:
				print form.errors
		else:
			form = EventForm(request.POST, request.FILES)
			if form.is_valid:
				print 'The form is valid'
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
def view_edit_event(request):
	context = {}
	print request.GET
	event_track_num = request.GET.get('event_track_num')
	event_obj = Event.objects.get(tracking_number=event_track_num)
	event_form = EventForm(instance=event_obj)
	context['event_track_num'] = event_track_num
	context['event_form'] = event_form
	return render(request,'ynladmin/edit_event.html',context)












