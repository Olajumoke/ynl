from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [
        url(r'^wallet/details/$',views.view_wallet, name="wallet"),

]