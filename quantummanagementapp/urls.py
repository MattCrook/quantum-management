# from quantummanagementapp.views.admin_users.auth.actions import login_user, logout_user, admin_user
from quantummanagementapp.views.admin_users.auth.actions import admin_user, login_user
from quantummanagementapp.views.auth0 import dashboard, index, logout
from .views.home.landing_page import landing_page
from django.urls import path
from django.conf.urls import include, url
from quantummanagementapp import views
from .views import *
# from quantummanagementapp.index_view import index, dashboard, logout

app_name = "quantummanagementapp"

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),

    path('admin/', admin_user, name='admin'),
    path('', index),
    path('dashboard/', dashboard),
    path('logout/', logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
