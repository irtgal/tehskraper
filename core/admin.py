from django.contrib import admin
from .models import *

class StoryAdmin(admin.ModelAdmin):
	list_display = ['__str__']

admin.site.register(Story, StoryAdmin)

