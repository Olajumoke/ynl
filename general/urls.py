from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [
            url(r'^$', views.homepage, name='homepage'),
            # url(r'^signup/Page/$', views.userregister,  name="userregister"),
            # url(r'^login/Page/$', views.userlogin,  name="login"),
            url(r'^signup/Page/$', views.register,  name="register"),
            url(r'^login/Page/$', views.user_login,  name="login"),

  
	]