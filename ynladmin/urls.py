from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [

            # url(r'^admin/home/$', views.admin_home, name='adminHome'),
            url(r'^admin/all/(?P<pages_to>.+)/$', views.admin_pages, name='admin_pages'),
            url(r'^admin/create-event/$', views.create_event, name='create_event'),
            url(r'^admin/delete-event/(?P<event_id>[\w]+)/$', views.delete_event, name='delete_event'),
            url(r'^admin/delete-user/(?P<user_id>[\w]+)/$', views.delete_user, name='delete_user'),
            url(r'^admin/edit-event/$', views.view_edit_event, name='view_edit_event'),
            url(r'^admin/edit-user/$', views.edit_user, name='edit_user'),

    ]

