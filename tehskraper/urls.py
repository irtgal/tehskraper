from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
	url('^', include('core.urls')),

]
