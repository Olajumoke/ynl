from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [

			url(r'^signup/Page/$', views.register,  name="register"),
			url(r'^login/Page/$', views.user_login,  name="login"),
  
		]