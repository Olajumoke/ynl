# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from paystack.resource import TransactionResource
import string, random, ast, json
from general.models import UserAccount
from .models import Bank
# Create your views here.

def view_wallet(request):
    return render(request, 'wallet/topup.html') 


def generate_purchaseRef():
    rand = ''.join(
             [random.choice(
                 string.ascii_letters + string.digits) for n in range(16)]) 
    return rand

def purchase_ref():
    ref = generate_purchaseRef()#+ "|%s" %obj_id
    while Bank.objects.filter(ref_no = ref):
            ref = generate_purchaseRef() 
    print "ref",ref
    return ref



    

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
        
        secret_key = 'sk_test_9fe140b2bf798accdc2aade269cac47bc2de7ecc'
        random_ref = purchase_ref()
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
        response = json.loads(verify)
        ref = ast.literal_eval(response)
        print ref
        ref_no = data['reference']
        print ref_no
        bank_record = Bank.objects.create(user=request.user,txn_type="Add",amount=value, ref_no=random_ref,
                        payment_gateway_tranx_id=verify['reference'],message=verify['message'], status=verify['status'],created_at=timezone.now)
        bank_record.save()
        #client.charge(None,amount,email,random_ref)
        #print client.charge() # Charge an already exsiting client
    return render(request, 'wallet/topup.html')
   
