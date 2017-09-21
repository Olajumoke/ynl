# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import UserAccount, Event, Comments, MessageCenter, MessageCenterComment, Likes, Referral
# Register your models here.



# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'category',)


class UserAccountAdmin(admin.ModelAdmin):
    search_fields = ['user__email']

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Comments)
admin.site.register(MessageCenterComment)
admin.site.register(MessageCenter)
admin.site.register(Likes)
admin.site.register(Referral)