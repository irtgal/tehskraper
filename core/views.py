from rest_framework import generics
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q

from .scripts import *
from .models import Story
from .serializers import StorySerializer

@api_view(('GET',))
def get_stories(request):
	#get_slotech()
	#get_monitor()
	last_id = request.GET.get('last_story', False)
	if last_id:
		last_date = get_object_or_404(Story, id=last_id).date
		queryset = Story.objects.filter(Q(date__lt=last_date)).order_by("-date")[:10]
		if not queryset:
			return Response({'error': 'Ni več novic'})
	else:

		queryset = Story.objects.all().order_by("-date")[:10]
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Novo'})

@api_view(('GET',))
def get_page(request, page_name):
	last_id = request.GET.get('last_story', False)
	if last_id:
		last_date = get_object_or_404(Story, id=last_id).date
		queryset = Story.objects.filter(Q(date__lt=last_date, page=page_name)).order_by("-date")[:10]
		if not queryset:
			return Response({'error': 'Ni več novic'})

	else:
		queryset = Story.objects.filter(page=page_name).order_by("-date")[:10]
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': queryset[0].pretty_page()})

@api_view(('GET',))
def get_saved(request):
	queryset = Story.objects.filter(saved=True).order_by("-saved_date")
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Shranjeno'})

@api_view(('GET',))
def search(request, query):
	queryset = Story.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
	serializer = StorySerializer(queryset, many=True)
	return Response({'stories': serializer.data, 'app_title': 'Rezultati za'})


@api_view(('GET',))
def save(request, story_id):
	story = get_object_or_404(Story, id=story_id)
	story.saved = not story.saved
	story.saved_date = timezone.now() if story.saved == True else None
	story.save()
	return Response(story.saved)

@api_view(('GET',))
def seen(request, story_id):
	story = get_object_or_404(Story, id=story_id)
	story.seen = True
	story.save()
	return Response(True)