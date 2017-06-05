from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponse , HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from general.forms import UserForm

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
import random, datetime
import urllib
import time
from django.core.urlresolvers import reverse
import json
from django.db.models import Sum
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage


# Create your views here.


def homepage(request):
	context = {}
	template_name = 'general/homepage.html'
	return render(request, template_name, context)

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
				return redirect(reverse('general:homepage'))
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
				
				return redirect('general:login')
			else:
				print form.errors
	else:
		form = UserForm()
	return render(request, 'general/registration.html', {'form': form})