from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [
            url(r'^admin/home/$', views.admin_home, name='adminHome'),
            url(r'^admin/events/(?P<pages_to>.+)/$', views.admin_pages, name='admin_pages'),
            url(r'^admin/create_event/$', views.create_event, name='create_event'),
    ]

