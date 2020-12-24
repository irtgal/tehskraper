from rest_framework import generics
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .scripts import *
from .models import Story
from .serializers import StorySerializer

@api_view(('GET',))
def get_stories(request):
	get_slotech()
	get_monitor()
	queryset = Story.objects.all().order_by("-date")[:30]
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Novo'})

@api_view(('GET',))
def get_page(request, page_name):
	queryset = Story.objects.filter(page=page_name).order_by("-date")[:30]
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': queryset[0].pretty_page()})

@api_view(('GET',))
def get_saved(request):
	queryset = Story.objects.filter(saved=True).order_by("-saved_date")[:30]
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Shranjeno'})

@api_view(('GET',))
def search(request, query):
	print(query)
	queryset = Story.objects.filter(title__unaccent__icontains=query).order_by("-date")[:30]
	print(query)
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Rezultati za'})





@api_view(('GET',))
def save(request, story_id):
	story = get_object_or_404(Story, id=story_id)
	story.saved = not story.saved
	story.saved_date = timezone.now() if story.saved == True else None
	print(f'Shranjeno: {story.saved_date}')
	story.save()
	return Response(story.saved)

@api_view(('GET',))
def seen(request, story_id):
	story = get_object_or_404(Story, id=story_id)
	story.seen = True
	story.save()
	return Response(True)