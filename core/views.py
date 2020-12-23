from rest_framework.response import Response
from rest_framework import generics
from .scripts import *
from .models import Story
from .serializers import StorySerializer

class StoriesView(generics.RetrieveAPIView):
	queryset = Story.objects.all().order_by("-date")[:3]


	def get(self,request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = StorySerializer(queryset, many=True)
		print(serializer.data)
		return Response(serializer.data)
		