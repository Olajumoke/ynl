from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, HttpResponse , HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from general.forms import UserForm, UserAccountForm, UserProfileForm, MessageCenterCommentForm, RepliesForm
from general.models import UserAccount, Event, MessageCenter, MessageCenterComment, Comments
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
from wallet.account_standing import account_standing
from wallet.models import Bank
from gameplay.models import Gameplay
from general.staff_access import *
# Create your views here.

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


def homepage(request):
    context = {}
    template_name = 'general/homepage.html'
    # context['most_recent'] = most_recent
    events_all = Event.objects.filter(deleted=False)
    all_events = paginate_list(request,events_all,4)
    balance = account_standing(request,request.user)
    categories = []
    try:
        most_recent = events_all[0]
        context['most_recent'] = most_recent
    except:
        pass
    for event in events_all:
        if event.category in categories:
            pass
        else:
            categories.append(event.category)
    context['categories'] = categories
    context['events'] = all_events
    context['balance'] = balance
    return render(request, template_name, context)


def getCategory(request,value):
	context = {}
	template_name = 'general/homepage.html'
	# context['most_recent'] = most_recent
	value_to_upperCase = value.upper()
	events_all = Event.objects.filter(deleted=False,category=value_to_upperCase)
	all_events = paginate_list(request,events_all,4)
	categories = []
	try:
		most_recent = events_all[0]
		context['most_recent'] = most_recent
	except:
		pass
	for event in events_all:
		if event.category in categories:
			pass
		else:
			categories.append(event.category)
	context['categories'] = categories
	context['events'] = all_events
	return render(request, template_name, context)



def user_login(request):
    if request.method == "POST":
        
		username = request.POST.get('username')
		password = request.POST.get('password')
		try :
			username = User.objects.get(email=username).username
		except Exception as e:
			print "e", e
			try:
				username = User.objects.get(username=username).username
				username = username
			except Exception as e:
				return render(request, 'general/sign_in.html', {'error_msg':"Invalid login details supplied."})
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
    events_all = Event.objects.filter(deleted=False)
    categories = []
    balance = account_standing(request,request.user)
    for event in events_all:
        if event.category in categories:
            pass
        else:
            categories.append(event.category)
    context['categories'] = categories
    events_all = Event.objects.filter(deleted=False)
    event_obj = Event.objects.get(pk=pk)
    try:
        next_event = Event.get_previous_by_created_on(event_obj)
        if next_event.deleted:
        	pass
        else:
        	context['next_event'] = next_event
    except:
        pass
    try:
        previous_event = Event.get_next_by_created_on(event_obj)
        if previous_event.deleted:
        	pass
        else:
        	context['previous_event'] = previous_event
    except:
        pass

    event_pk = event_obj.pk
    most_recent = events_all[0]
    today = timezone.now()
    context['event'] = event_obj
    context['today'] = today.date()
    context['all_events'] = events_all
    context['event_pk'] = event_pk
    context['most_recent'] = most_recent
    context['balance'] = balance
    
    return render(request, 'general/magazine-single-article.html',context)


@login_required
def user_profile(request):
	# try:
	# 	user_account = UserAccount.objects.get(user=request.user)
	# except Exception as e :
	# 	print "e", e
    if UserAccount.objects.filter(user=request.user).exists():
        print "I exist"
        user = UserAccount.objects.get(user=request.user)
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, instance=request.user)
            user_account_form = UserAccountForm(request.POST, request.FILES, instance=user)
            if user_account_form.is_valid() and user_form.is_valid():
                form1 = user_form.save()
                form1.first_name = request.POST.get('first_name')
                form1.last_name = request.POST.get('last_name')
                form1.save()
                form2 = user_account_form.save(commit=False)
                form2.user = form1
                form2.created_on = timezone.now()
                form2.save()
                #user =  UserAccount.objects.get(user=request.user)
                messages.success(request, "User Details Updated Succesfully!!!")
                return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                print user_account_form.errors, user_form.errors
        else:
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
                #user =  UserAccount.objects.get(user=request.user)
                return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                form1 = UserProfileForm(instance=request.user)
                form2 = UserAccountForm()
                user = None
                print user_account_form.errors, user_form.errors
                
        else:
            form1 = UserProfileForm(instance=request.user)
            form2 = UserAccountForm()
            user = None
	return render(request, 'general/profile.html', { 'form1':form1, 'form2':form2, 'user':user})


@login_required
@user_passes_test(staff_check_for_gameplay, login_url='/backend/admin/all/events/', redirect_field_name=None)
def user_account(request):
	try:
	 	user = UserAccount.objects.get(user=request.user)
	except Exception as e :
		print "e", e
		user = None
	balance = account_standing(request,request.user)
	game = Gameplay.objects.filter(user=user)
	game_won = game.filter(decision="WIN")
	print "game-won", game_won
	return render(request, 'general/user_account.html', {'user':user, 'balance':balance, 'game':game, 'game_won':game_won})


def about_us(request):
	
	return render(request, 'general/about_page.html', {})


def contact(request):
	return render(request, 'general/contact.html', {})

# def account_activation(request):
# 	if UserAccount.objects.filter(user=request.user).exists():
# 		print "I exist"
# 	
# 	return render(request, 'general/profile.html', {})


@login_required
def user_messages(request):
	context = {}
	try:
	 	user = UserAccount.objects.get(user=request.user)
	except Exception as e :
		print "e", e
		user = None
	if request.method == 'POST':
		if request.POST.has_key('messages_search'):
			context = {}
			query = request.POST.get('search_for')
			query = request.POST.get('search_for')
			new_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), new=True)
			replied_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), replied=True)
			archived_messages = MessageCenter.objects.filter((Q(subject__icontains=query) | Q(user__username__icontains=query)), archive=True)
			comment_form = MessageCenterCommentForm()
			context['comment_form'] = comment_form
			context['new_messages'] = new_messages
			context['replied_messages'] = replied_messages
			context['archived_messages'] = archived_messages
			context['new_count'] = new_messages.count()
			context['replied_count'] = replied_messages.count()
			context['archived_count'] = archived_messages.count()
			context['user'] = user
			template_name = 'general/user_messages.html'
			return render(request,template_name,context)
		else:
			rp = request.POST
			print "rp: ", rp	
			message_obj = MessageCenter.objects.create(
				subject=rp.get('subject'),
				message=rp.get('message'),
				user=request.user,
				new=True
				)
			message_obj.save()
			comment_obj = MessageCenterComment.objects.create(
				message=rp.get('message'),
				message_obj=message_obj,
				user=request.user)
			messages.success(request,'Message sent successfully')
			return redirect(request.META['HTTP_REFERER'])
	else:
		rg = request.GET
		print 'rg:',rg
		context = {}
		new_messages = MessageCenter.objects.filter(new=True)
		replied_messages = MessageCenter.objects.filter(replied=True)
		archived_messages = MessageCenter.objects.filter(archive=True)
		comment_form = MessageCenterCommentForm()
		context['comment_form'] = comment_form
		context['new_messages'] = new_messages
		context['replied_messages'] = replied_messages
		context['archived_messages'] = archived_messages
		context['new_count'] = new_messages.count()
		context['replied_count'] = replied_messages.count()
		context['archived_count'] = archived_messages.count()
		context['user'] = user
		template_name = 'general/user_messages.html'
		return render(request,template_name,context)


def user_comment(request):
	rp = request.POST
	print rp
	event_obj = Event.objects.get(pk=rp.get('event_pk'))
	create_comment = Comments.objects.create(username=rp.get('name'),text=rp.get('comment'),email=rp.get('mail'),event=event_obj)
	messages.success(request,'Message sent successfully')
	return redirect(request.META['HTTP_REFERER'])



@login_required
def view_comment_message(request):
	context = {}
	if request.method == 'POST':
		print 'rp:',request.POST
		message_obj = MessageCenter.objects.get(id=request.POST.get('msg_id'))
		comment_obj = MessageCenterComment.objects.create(
			message=request.POST.get('message'),
			message_obj=message_obj,
			image_obj=request.FILES.get('image_obj'),
			user=request.user)
		messages.success(request,'Message sent successfully')
		return redirect(request.META['HTTP_REFERER'])

	else:
		print request.GET
		template_name = ""
		if request.GET.get('identifier') == 'comment':
			template_name = 'general_snippets/messageComments.html'
		else:
			template_name = 'general_snippets/viewMessages.html'
		message_id = request.GET.get('message_id')
		message_obj = MessageCenter.objects.get(id=message_id)
		print "msg_obj:", message_obj
		all_comments = message_obj.getComments()
		comment_form = MessageCenterCommentForm()
		context['comment_form'] = comment_form
		context['all_comments'] = all_comments
		context['message_id'] = message_id
		return render(request,template_name,context)
	

