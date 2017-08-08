# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, redirect
#from paystack.resource import TransactionResource
import string, random, ast, json
from general.models import UserAccount
from .models import Bank
from wallet.account_standing import account_standing, bank_codes
from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from wallet.Transfer import Transfer
from django.contrib import messages
from django.core.urlresolvers import reverse
from general.views import paginate_list
from gameplay.models import Gameplay
from django.contrib.auth.decorators import login_required,user_passes_test
from general.staff_access import *
# Create your views here.

paystack_secret_key = "sk_test_9fe140b2bf798accdc2aade269cac47bc2de7ecc"  
paystack = Paystack(secret_key=paystack_secret_key)

@login_required
@user_passes_test(staff_check_for_gameplay, login_url='/backend/admin/all/events/', redirect_field_name=None)
def view_wallet(request):
    try:
        user = UserAccount.objects.get(user=request.user)
    except Exception as e :
        print "e", e
        user = None
    game    = Gameplay.objects.filter(user=user)
    balance = account_standing(request,request.user)
    wallet = paginate_list(request, Bank.objects.filter(user=request.user),5)
    
    return render(request, 'wallet/topup.html', {'balance':balance, 'wallet':wallet, 'user':user, 'game':game}) 


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

@login_required
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
    data = response_dict.get('data')
    print 'status', data['status']
    if data['status'] == 'success':
        status = "Successful"
    else:
        status = data['status']
    bank_record = Bank.objects.get(ref_no=ref)
    bank_record.status = status
    bank_record.message = data['gateway_response']
    bank_record.save()
    return redirect('wallet:wallet')



def create_recipient(request):
    # user = UserAccount.objects.get(user=request.user)
    # first_name = user.user.first_name
    # last_name = user.user.last_name
    # name = first_name + last_name
    # print name
    # description = "Withdrawal from YNLwallet"
    # account_number = user.account_number
    # bank_code = '058'
    # response = Transfer.create_recipient(type='nuban',name=name,description=description,
    #                                      account_number=account_number,bank_code=bank_code)
    # print "response:", response
    # data = response.get('data')
    # recipient_code = data['recipient_code']
    # amount = 10000
    # reason = "Withdrawal from YNLwallet"
    # transfer = Transfer.transfer(source='balance',reason=reason,amount=amount,recipient=recipient_code)
    # print "transfer:", transfer
    # verify = transfer.get('data')
    transfer_code = 'TRF_2o8n1mj1zogql3l'
    otp = 782008
    finalize = Transfer.finalize_transfer(transfer_code=transfer_code,otp=otp)
    return redirect('wallet:wallet')
    
@login_required
def cash_out(request):
    if request.method == "POST":
        credit = account_standing(request, request.user)
        print "credit:", credit
        amount = float(request.POST.get('amount'))
        print amount > credit
        if amount > credit:
            messages.warning(request, "You do not have Sufficient money in your wallet!!!")
        else:
            ref = purchase_ref()
            user = UserAccount.objects.get(user=request.user)
            bank = user.bank
            cash_out = Bank.objects.create(user=request.user,txn_type="Remove",amount=amount, ref_no=ref,status="Transfer",
                            created_at=timezone.now(), bank=bank,message="Cash out from YNLwallet to Bank")
            messages.info(request, "Your request is being processed!!!")
    return redirect('wallet:wallet')


def initiate_transfer(request):
    print "I started transfer"
    pk = request.GET.get('pk')
    record = Bank.objects.get(pk=pk)
    user = UserAccount.objects.get(user=record.user)
    first_name = user.user.first_name
    last_name = user.user.last_name
    name = first_name +"" + last_name
    print name
    description = "Withdrawal from YNLwallet"
    account_number = user.account_number
    bank_code = bank_codes(user.bank)
    response = Transfer.create_recipient(type='nuban',name=name,description=description,
                                         account_number=account_number,bank_code=bank_code)
    print "response:", response
    data = response.get('data')
    recipient_code = data['recipient_code']
    amount = record.amount * 100
    reason = "Withdrawal from YNLwallet"
    transfer = Transfer.transfer(source='balance',reason=reason,amount=amount,recipient=recipient_code)
    print "transfer:", transfer
    verify = transfer.get('data')
    transfer_code = verify['transfer_code']
    return render(request, 'wallet/finalize_transfer.html', {'transfer_code':transfer_code, 'ref':record.ref_no})
        
def finalize_transfer(request):
    print "i got here"
    if request.method == "POST":
        otp = str(request.POST.get('otp'))
        transfer_code = str(request.POST.get('transfer_code'))
        ref = request.POST.get('ref')
        finalize = Transfer.finalize_transfer(transfer_code=transfer_code,otp=otp)
        print "finalize:", finalize
        verify= finalize.get('data')
        verify_list = verify[0]
        status = verify_list['status']
        print "status",status
        bank = Bank.objects.get(ref_no=ref)
        if status == "success":
            bank.status = "Successful"
        else:
            bank.status = "Declined"
        bank.payment_gateway_tranx_id = transfer_code
        bank.save()
        return redirect(reverse('ynladmin:admin_pages', args=['payment']))

def resend_otp(request):
    print "i got to dis place"
    transfer_code = str(request.GET.get('transfer_code'))
    reason = 'resend_otp'
    response = Transfer.resend_otp(transfer_code=transfer_code)
    print "response", response
    return response
