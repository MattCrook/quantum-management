
# from django.urls import path
# from rest_framework import views, serializers, status
# from rest_framework.response import Response
# from rest_framework import routers
# from django.conf.urls import url, include
# from django.urls import path
# from quantummanagementapp.models import *

from quantummanagementapp.views.admin_users.auth.actions import login_user, logout_user, admin_user
from .views.home.landing_page import landing_page
from django.urls import path
from django.conf.urls import include
from quantummanagementapp import views
from .views import *

app_name = "quantummanagementapp"

urlpatterns = [
    # path('', landing_page, name='landing_page'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),

    path('admin/', admin_user, name='admin'),
    path('', views.index),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
