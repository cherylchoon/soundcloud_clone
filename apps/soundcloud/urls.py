from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^stream$', index, name='stream'),
    url(r'^logout$', logout, name='logout'),
    url(r'^update_profile/(?P<id>\d+)$', update_profile, name='update_profile'),
    url(r'^user/(?P<id>\d+)$', user, name='user'),
    url(r'^follow$', follow, name='follow'),
    url(r'^unfollow$', unfollow, name='unfollow'),
    url(r'^search$', search, name='search'),
    url(r'^stream/addcomment$', create_comment, name='addcomment'),
    url(r'^stream/deletecomment$', delete_comment, name='deletecomment'),
]
