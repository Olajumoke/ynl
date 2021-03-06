from django.conf.urls import patterns, include, url
from django.conf import settings
import views


urlpatterns = [
            url(r'^$', views.homepage, name='homepage'),
            url(r'^signup/Page/$', views.register,  name="register"),
            url(r'^login/Page/$', views.user_login,  name="login"),
            url(r'^user-logout/$', views.user_logout,  name="logout"),
            url(r'^events-page/$', views.events_page,  name="events"),
            url(r'^event/details/(?P<pk>[-\w]+)/$',views.event_details, name="event_details"),
            url(r'^user/dashboard/$',views.user_account, name = "user_account"),
            url(r'^user/profile/$',views.user_profile, name = "profile"),
            url(r'^category/(?P<value>.+)$',views.getCategory, name = "getCategory"),
            url(r'^about/$',views.about_us, name = "about_us"),
            url(r'^Contact-us/$',views.contact, name = "contact"),
            url(r'^user/messages/$',views.user_messages, name = "messages"),
            url(r'^userComment/$',views.user_comment, name = "user_comment"),
            url(r'^search-results/(?P<action>[-\w]+)/$',views.user_search, name = "user_search"),
            url(r'^user/comments/$',views.view_comment_message, name = "view_comment_message"),
            url(r'^like/comments/(?P<action>[-\w]+)/(?P<pk>.+)/$',views.like_comments, name = "like_comments"),
            url(r'^check/referral/$', views.check_referrer, name="check_referrer"),
            #url(r'^reply/comment/$', views.reply_comment,name="reply_comment"),


]

