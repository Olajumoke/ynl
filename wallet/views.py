# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, redirect
#from paystack.resource import TransactionResource
import string, random, ast, json
from general.models import UserAccount
from .models import Bank
from wallet.account_standing import account_standing
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
# Create your views here.

paystack_secret_key = "sk_test_9fe140b2bf798accdc2aade269cac47bc2de7ecc"  
paystack = Paystack(secret_key=paystack_secret_key)


def view_wallet(request):
    balance = account_standing(request,request.user)
    wallet = Bank.objects.filter(user=request.user)
    
    return render(request, 'wallet/topup.html', {'balance':balance, 'wallet':wallet}) 


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
        
        #secret_key = 'sk_test_9fe140b2bf798accdc2aade269cac47bc2de7ecc'
        random_ref = purchase_ref()
        request.session['ref_no']= random_ref
        response = Transaction.initialize(reference=random_ref, 
                                  amount=amount, email=email)
        print 'response:', response
        data = response.get('data')
        print "data:", data
        authorization_code=data['access_code']
        print "access_code", authorization_code
        url = data['authorization_url']
        print 'url', url
        bank_record = Bank.objects.create(user=request.user,txn_type="Add",amount=value, ref_no=random_ref,
                        created_at=timezone.now())
        bank_record.save()
    return redirect(url)
        # response = Transaction.charge(reference=random_ref, 
        #                       authorization_code=authorization_code,
        #                       email=email,
        #                       amount=amount)
        # response_dict = Transaction.verify(reference=random_ref)
        # print "response_dict", response_dict
        #test_email = email
        #test_amount = amount
        #plan = 'Basic'
        # client = TransactionResource(secret_key, random_ref)
        # response = client.initialize(amount,email)
        # print"response",response
        # client.authorize() # Will open a browser window for client to enter card details
        # verify = client.verify() # Verify client credentials
        # print "verify", verify
        # print type(verify)
        # ref = verify.get('data')
        # print ref
        
        #client.charge(None,amount,email,random_ref)
        #print client.charge() # Charge an already exsiting client
    # return render(request, 'wallet/topup.html')
   
   
def verify_payment(request):
    ref = request.session['ref_no']
    response_dict = Transaction.verify(reference=ref)
    # data = response.get('data')
    print 'status', response_dict['status']
    if response_dict['status'] == True:
        status = "Successful"
    else:
        status = response_dict['status']
    bank_record = Bank.objects.get(ref_no=ref)
    bank_record.status = status
    bank_record.message = response_dict['message']
    bank_record.save()
    return redirect('wallet:wallet')


