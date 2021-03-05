from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from .views import *

urlpatterns = [
	url(r'^$', get_stories, name="get_stories"),
	url(r'^page/(?P<page_name>\w+)/$', get_page, name="get_page"),
	url(r'^saved/$', get_saved, name="get_saved"),
	url(r'^search/(?P<query>.+)/$', search, name="search"),
	url(r'^save/(?P<story_id>\d+)/$', save, name="save"),
	url(r'^seen/(?P<story_id>\d+)/$', seen, name="seen"),
	url(r'^stats/$', get_stats, name="get_stats"),
]
