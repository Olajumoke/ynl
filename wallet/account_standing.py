from django.contrib.auth.models import User
from general.models import UserAccount
from wallet.models import Bank
from django.db.models import Q, Sum



def account_standing(request, user):
    if not request.user.is_authenticated():
        return 0, 0
    #user = User.objects.select_related('useraccount').get(username = request.user)

    # useraccount = UserAccount.objects.get(user = user)
    # print "useraccount country",useraccount.country

    #user.get_profile()
    #user = useraccount.user
    #user_country = user.useraccount.country

    #1. Calculate sum of user's approved (bank) and successful (card) payments
    #added_payments = SokoPay.objects.user_add_jejepay(request.user).aggregate(Sum('amount'))
    added_payments = Bank.objects.user_add_credit(user).aggregate(Sum('amount'))
        
    if added_payments['amount__sum'] == None:
        total_added_payments = 0
    # else:
    #     if not useraccount.country == "USA":
    #         total_added_payments_N = added_payments['amount__sum']
    else:
        total_added_payments = added_payments['amount__sum']
    print "total added payments", total_added_payments
    #used_payments = SokoPay.objects.jejepay_withdrawals(request.user).aggregate(Sum('amount'))
    used_payments = Bank.objects.user_remove_credit(user).aggregate(Sum('amount'))
    if used_payments['amount__sum'] == None:
        total_used_payments = 0
    # else:
    #     if not useraccount.country == "USA":
    #         total_used_payments_N = used_payments['amount__sum']
    else:
        total_used_payments = used_payments['amount__sum']
    print "total used payments", total_used_payments

    #user_approved_refunds = SokoPay.objects.user_refund_jejepay(request.user).aggregate(Sum('amount'))
    # user_approved_refunds = SokoPay.objects.user_refund_jejepay(user).aggregate(Sum('amount'))
    # if user_approved_refunds['amount__sum'] == None:
    #     total_user_refunds_N = 0
    # # else:
    # #     if not useraccount.country == "USA":
    # #         total_user_refunds_N = added_payments['amount__sum']
    # else:
    #     total_user_refunds_N = user_approved_refunds['amount__sum']
    # 
    # print "total user refunds", total_user_refunds_N

    #Sum of orders and shipments costs

    #4. Calculate the user's credit standing as #1 - #2 - #3
    user_credit_amount = total_added_payments - total_used_payments
    # if not useraccount.country == "United States":
    #     dollar_exchange_rate = marketingmember_costcalc(request,useraccount.country).dollar_exchange_rate
    #     user_credit_amount_D = user_credit_amount_N / float(dollar_exchange_rate)
    #     useraccount.credit_amount_N = user_credit_amount_N
    # else:
    #     user_credit_amount_D = user_credit_amount_N
    #     user_credit_amount_N = 0
    #     useraccount.credit_amount_N = 0
    #     print "USER", useraccount.credit_amount_N
    #return {'user_credit_amount_N': user_credit_amount_N, 'user_credit_amount_D': user_credit_amount_D}
    #useraccount.credit_amount_N = user_credit_amount_N
    # useraccount.credit_amount_D = user_credit_amount_D
    # useraccount.save()

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
