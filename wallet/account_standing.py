from django.contrib.auth.models import User
from general.models import UserAccount
from wallet.models import Bank
from django.db.models import Q, Sum



def account_standing(request, user):
    if not request.user.is_authenticated():
        return 0, 0
    
    added_payments = Bank.objects.user_add_credit(user).aggregate(Sum('amount'))
        
    if added_payments['amount__sum'] == None:
        total_added_payments = 0
    
    else:
        total_added_payments = added_payments['amount__sum']
    print "total added payments", total_added_payments
    
    used_payments = Bank.objects.user_remove_credit(user).aggregate(Sum('amount'))
    if used_payments['amount__sum'] == None:
        total_used_payments = 0
    
    else:
        total_used_payments = used_payments['amount__sum']
    print "total used payments", total_used_payments

    #4. Calculate the user's credit standing as #1 - #2 - #3
    user_credit_amount = total_added_payments - total_used_payments

    return round(user_credit_amount, 2)


def bank_codes(bank):
    if bank == "ACCESS BANK":
        code = '044'
    elif bank == 'CITIBANK':
        code = "023"
    elif bank == 'DIAMOND BANK':
        code = "063"
    elif bank == 'ECOBANK':
        code = "050"
    elif bank == 'FIDELITY BANK':
        code = "070"
    elif bank == 'FIRST CITY MONUMENT BANK':
        code = "214"
    elif bank == 'FIRST BANK':
        code = "011"
    elif bank == 'GUARANTY TRUST BANK':
        code = "058"
    elif bank == 'HERITAGE BANK':
        code = "030"
    elif bank == 'KEYSTONE BANK':
        code = "082"
    elif bank == 'SKYE BANK':
        code = "076"
    elif bank == 'STANBIC IBTC':
        code = "221"
    elif bank == 'STANDARD CHARTERED BANK':
        code = "068"
    elif bank == 'STERLING BANK':
        code = "232"
    elif bank == 'UNION BANK OF NIGERIA':
        code = "032"
    elif bank == 'UNITED BANK OF AFRICA':
        code = "033"
    elif bank == 'UNITY BANK':
        code = "215"
    elif bank == 'WEMA BANK':
        code = "035"
    else:
        code = "057"
    return code
