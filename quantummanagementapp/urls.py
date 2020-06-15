
# from django.urls import path
# from rest_framework import views, serializers, status
# from rest_framework.response import Response
# from rest_framework import routers
# from django.conf.urls import url, include
# from django.urls import path
# from quantummanagementapp.models import *

from quantummanagementapp.views.admin_users.auth.actions import *
from django.urls import include, path

app_name = "quantummanagementapp"


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('libraryapp.urls')),
    # path('home/', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]
