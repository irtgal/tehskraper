from rest_framework.response import Response
from rest_framework import generics
from .scripts import *
from .models import Story
from .serializers import StorySerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
import json

@api_view(('GET',))
def get_stories(request):
	#get_slotech()
	#get_monitor()
	queryset = Story.objects.all().order_by("-date")[:15]
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Novo'})

@api_view(('GET',))
def get_page(request, page_name):
	queryset = Story.objects.filter(page=page_name).order_by("-date")
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': queryset[0].pretty_page()})

@api_view(('GET',))
def save(request, story_id):
	story = get_object_or_404(Story, id=story_id)
	story.saved = not story.saved
	story.save()
	return Response(story.saved)

@api_view(('GET',))
def seen(request, story_id):
	story = get_object_or_404(Story, id=story_id)
	story.seen = True
	story.save()
	return Response(True)