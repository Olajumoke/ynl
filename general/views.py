from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponse , HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from general.forms import UserForm, UserAccountForm, UserProfileForm
from general.models import UserAccount, Event
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
import random, datetime
import urllib
import time
from django.core.urlresolvers import reverse
import json
from django.db.models import Sum
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from django.utils import timezone

# Create your views here.


def homepage(request):
	context = {}
	event_obj = Event.objects.filter(deleted=False)
	template_name = 'general/homepage.html'
	context['events'] = event_obj
	return render(request, template_name, context)


def paginate_list(request, objects_list, num_per_page):
    paginator   =   Paginator(objects_list, num_per_page) # show number of jobs per page
    page  = request.GET.get('page')
    try:
        paginated_list  = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        paginated_list   =   paginator.page(1)
    except  EmptyPage:
        #if page is out of range(e.g 9999), deliver last page of results
        paginated_list      =   paginator.page(paginator.num_pages)
    return paginated_list


def user_login(request):
    if request.method == "POST":
        
		username = request.POST.get('username')
		password = request.POST.get('password')
		if '@' in username :
			username = User.objects.get(email=username).username
		else:
			username = username
		user = authenticate(username=username, password=password)
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:

				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)                  
				if user.is_staff:
					response =  redirect(reverse('ynladmin:admin_pages', args=['events']))
					return response    
				else:
					response = redirect(reverse('general:homepage'))
					return response
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print "Invalid login details: {0}, {1}".format(username, password)
			return render(request, 'general/sign_in.html', {'error_msg':"Invalid login details supplied."})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'general/sign_in.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return redirect(reverse('general:homepage'))

def register(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		rp = request.POST
        #print "form", form
		if User.objects.filter(username = rp.get('username')).exists():
			print 'username exists'
			return render(request, 'general/registration.html', {'form': form,'username_is_taken':True})                
		if User.objects.filter(email = rp.get('email')).exists():
			print 'email exists'                
			return render(request, 'general/registration.html', {'form': form,'email_taken':True})                
		else:
			if form.is_valid():
				user = form.save(commit=False)
				password  = rp.get('password')
				password1   = rp.get('password1')
				if password != password1:
					return render(request, 'general/registration.html', {'form': form,'password_mismatch':True})
				if len(password) < 8:
					return render(request, 'general/registration.html', {'form': form,'password_too_short':True})
				# if password == rp.get('first_name'):
				# 	return render(request, 'general/registration.html', {'form': form,'password_same_as_first_name':True})
				if password.isalpha():
					return render(request, 'general/registration.html', {'form': form,'password_should_be_alphanumeric':True})
				# user = User.objects.create(username = rp.get('username'), email = rp.get('email').lower(),
				# 	first_name = rp.get('first_name'), last_name = rp.get('last_name'))
				user.set_password(user.password)
				user.save()
				''' try this '''
				# new_user_acc_obj = UserAccount.objects.create(user=user)
				
				return redirect('general:login')
			else:
				print form.errors
	else:
		form = UserForm()
	return render(request, 'general/registration.html', {'form': form})


def event_details(request,pk):
	context = {}
	event_obj = Event.objects.get(pk=pk)
	context['event'] = event_obj
	return render(request, 'general/magazine-single-article.html',context)

def user_profile(request):
	# try:
	# 	user_account = UserAccount.objects.get(user=request.user)
	# except Exception as e :
	# 	print "e", e
	if UserAccount.objects.filter(user=request.user).exists():
		print "I exist"
		user = UserAccount.objects.get(user=request.user)
		form1 = UserProfileForm(instance=request.user)
		form2 = UserAccountForm(instance=user)
		#print "form1", form1
	else:
		print "I do not exist"
		if request.method == "POST":
			#print "I got here", request.POST
			user_form = UserProfileForm(request.POST, instance=request.user)
			user_account_form = UserAccountForm(request.POST, request.FILES)
			if user_account_form.is_valid() and user_form.is_valid():
				form1 = user_form.save()
				form1.first_name = request.POST.get('first_name')
				form1.last_name = request.POST.get('last_name')
				form1.save()
				form2 = user_account_form.save(commit=False)
				form2.user = form1
				form2.created_on = timezone.now()
				form2.save()
				user =  UserAccount.objects.get(user=request.user)
				return redirect(request.META.get('HTTP_REFERER', '/'))
			else:
				print user_account_form.errors, user_form.errors
		else:
			form1 = UserProfileForm(instance=request.user)
			form2 = UserAccountForm()
			user = None
	return render(request, 'general/profile.html', { 'form1':form1, 'form2':form2, 'user':user})

def user_account(request):
	try:
	 	user = UserAccount.objects.get(user=request.user)
	except Exception as e :
		print "e", e
		user = None
	return render(request, 'general/user_account.html', {'user':user})

def account_activation(request):
	if UserAccount.objects.filter(user=request.user).exists():
		print "I exist"
	
	return render(request, 'general/profile.html', {})