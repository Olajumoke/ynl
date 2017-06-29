from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [
        url(r'^betting/$',views.betting, name = "betting"),
]