from django.contrib import admin
from django.urls import path
from rest_framework import views, serializers, status
from rest_framework.response import Response
from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path



router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('quantumapi.urls')),
]
