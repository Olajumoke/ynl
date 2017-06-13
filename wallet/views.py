# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from paystack.resource import TransactionResource
import string, random
from general.models import UserAccount
# Create your views here.

def view_wallet(request):
    return render(request, 'wallet/topup.html') 




def main(request):
    try:
        user_account = UserAccount.objects.get(user=request.user)
    except Exception as e :
        print "e", e
        return redirect('general:profile')
    if request.method == "POST":
        value = int(request.POST.get('amount'))
        print "value", value
        amount = value * 100
        print "amount", amount
        email = request.user.email
        rand = ''.join(
            [random.choice(
                string.ascii_letters + string.digits) for n in range(16)])
        secret_key = 'sk_test_9fe140b2bf798accdc2aade269cac47bc2de7ecc'
        random_ref = rand
        test_email = email
        test_amount = amount
        #plan = 'Basic'
        client = TransactionResource(secret_key, random_ref)
        response = client.initialize(amount,
                                     email
                                     )
        print"response",response
        client.authorize() # Will open a browser window for client to enter card details
        verify = client.verify() # Verify client credentials
        print "verify", verify
        #print(client.charge()) # Charge an already exsiting client
    return render(request, 'wallet/topup.html')
   
