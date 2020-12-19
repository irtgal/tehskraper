from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .scripts import *

def index(request):
	get_slotech()
	get_monitor()
	stories = Story.objects.all().order_by("-date")[:15]
	return render(request, 'index.html', {'stories': stories})
