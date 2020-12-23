from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from .views import StoriesView

urlpatterns = [
	url(r'^index/$', StoriesView.as_view(), name="story_view"),
]
