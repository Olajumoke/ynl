from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


from django.http import JsonResponse
from itertools import chain

from general.models import *
from django.db.models import Q, Count, Sum
from django.contrib import messages
from base64 import b64decode
import json, random
from django.core.files.base import ContentFile


# Create your views here.

@csrf_exempt
def getEvents(request):
	events_info = Event.objects.values("id", "category", "bet_question", "title", "created_on", "event_msg_body", "event_id")
	# print events_info
	return JsonResponse({"success": 1, "error": 0, 'events_info': list(events_info)})



@csrf_exempt
def login(request):
    if request.method == "POST":

        rp = request.POST
        print "rp:",rp
        email = rp['email']
        password = rp['password']
        if "@" in email:
            #authenticate user
            print "i got here and saw email"
            email = email
        else:
            print "its not an email"
            try:
                user_obj = User.objects.get(username=email)
                email = user_obj.email
            except Exception as e:
                print "the authentication failed because of ", e
                return JsonResponse({"success": 0, "error": 1, "error_message": "There is an error with the Email/Password combination!"})

        user = authenticate(email=email, password=password)

        print user

        if user is not None:
            if user.is_staff:
               
                   
                user_info = {"user_id": user.id, "full_name": user.get_full_name(),
                             "username": user.username, "email": email}

                events_count = Event.objects.all().count()
                str_events_count = str(events_count)
                return JsonResponse({"success": 1, "error": 0, "user_info": user_info, "events_count":str_events_count})

            
                             #"authorization_key": auth_key}
                #return HttpResponse(json.dumps({"success": 1, "error": 0,
                #                                "user_info": user_info}),
                #                content_type="application/json")
                # return JsonResponse({"success": 1, "error": 0, "user_info": user_info})
            else:
                return JsonResponse({"success": 0, "error": 1, "error_message": "Access Denied!!! This app is for members of STAFF ONLY!!!."})
                #return HttpResponse(json.dumps({"success": 0, "error": 1, "error_message": "Access Denied!!! This app is meant for STAFF ONLY!!!."}),
                #                content_type="application/json")
        else:
            #return HttpResponse(json.dumps({"success": 0, "error": 1, "error_message": "There was an error with the Email/Password combination!"}),
            #                    content_type="application/json")
            print "this is the isssue"
            return JsonResponse({"success": 0, "error": 1, "error_message": "There is an error with the Email/Password combination!"})
    else:
        #return HttpResponse(json.dumps({"success": 0, "error": 1}),
        #                    content_type="application/json")
        return JsonResponse({"success": 0, "error": 1})



@csrf_exempt
def validate_event(request):
    if request.method == 'POST':
        rp = request.POST
        print "rp:", rp
        return JsonResponse({"success": 1, "error": 0})
    else:
        print 'something went wrong'
        return JsonResponse({"success": 0, "error": 1})






