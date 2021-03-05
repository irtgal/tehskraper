from django.contrib import admin
from .models import *

def unseen(modeladmin, request, queryset):
    queryset.update(seen=False)
unseen.short_description = "Odstrani oznako za ogledano novico"


class StoryAdmin(admin.ModelAdmin):
	list_display = ['__str__']
	ordering = ['-date']
	actions = [unseen]

admin.site.register(Story, StoryAdmin)

