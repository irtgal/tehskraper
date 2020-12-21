from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json
from django.shortcuts import render
from .scripts import *

def index(request):
	#get_slotech()
	#get_monitor()
	stories = Story.objects.all().order_by("-date")[:15]
	stories_list = []
	for story in stories:
		stories_list.append({
			'id': story.id,
			'title': story.title,
			'summary': story.summary,
			'slug': story.slug,
			'seen': story.seen,
			'saved': story.saved,
			'page': story.pretty_page(),
			'date': story.pretty_date()

		})
	print(json.dumps(stories_list))
	return render(request, 'index.html', {'stories_json': json.dumps(stories_list)})
