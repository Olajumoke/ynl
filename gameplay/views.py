# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from general.models import Event, UserAccount
from django.shortcuts import render, redirect
from wallet.account_standing import account_standing
from django.utils import timezone
from wallet.models import Bank, Betpayments
from wallet.views import generate_purchaseRef, purchase_ref
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from gameplay.models import Gameplay
from django.core.urlresolvers import reverse
# Create your views here.


@login_required
def betting(request):
    balance = account_standing(request, request.user)
    if request.method == "POST":
        #print request.POST
        amount = float(request.POST.get('amount'))
        if amount > balance :
            messages.warning(request, "You do not have sufficient money in your wallet to place that bet")
            return redirect(request.META['HTTP_REFERER'])
        else:
            choice = str(request.POST.get('user-choice'))
            print 'choice',choice
            event = Event.objects.get(id=request.POST.get('event'))
            user = UserAccount.objects.get(user=request.user)
            try:
                gameplay = Gameplay.objects.get(event=event, user=user)
                print gameplay
                messages.warning(request, "You have already Participated in this Event")
                return redirect(request.META['HTTP_REFERER'])
            except Exception as e:
                print "e",e
            gameplay = Gameplay.objects.create(user=user,event=event,amount=amount,choice=choice,date=timezone.now(),status="OPEN")
            gameplay.save()
            random_ref = purchase_ref()
            bank_record = Bank.objects.create(user=request.user,txn_type="Remove",amount=amount, ref_no=random_ref,
                        created_at=timezone.now(), status="Successful", bank="Gameplay", message="Gameplay")
            bank_record.save()
            payment = Betpayments.objects.create(user=request.user,amount=amount,game=gameplay,date=timezone.now())
            payment.save()
            messages.success(request, 'Congratulations!!!! You have successfully placed your bet.')
            return redirect(request.META['HTTP_REFERER'])
    return redirect(reverse('general:homepage'))
            