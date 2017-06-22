from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [
            url(r'^$', views.homepage, name='homepage'),
            url(r'^signup/Page/$', views.register,  name="register"),
            url(r'^login/Page/$', views.user_login,  name="login"),
            url(r'^user-logout/$', views.user_logout,  name="logout"),
            url(r'^event/details/(?P<pk>[-\w]+)/$',views.event_details, name="event_details"),
            url(r'^user/dashboard/$',views.user_account, name = "user_account"),
            url(r'^user/profile/$',views.user_profile, name = "profile"),
            url(r'^user/messages/$',views.user_messages, name = "messages"),
            url(r'^user/comments/$',views.view_comment_message, name = "view_comment_message"),



]

