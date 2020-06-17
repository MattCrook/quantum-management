from quantummanagementapp.views.admin_users.auth.actions import login_user, logout_user, admin_user
# from quantummanagementapp.views.auth0 import dashboard, index, logout
from quantummanagementapp.views.home import landing_page, home
from django.urls import path
from django.conf.urls import include, url
from quantummanagementapp import views

app_name = "quantummanagementapp"

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('', include('django.contrib.auth.urls')),
    path('login/home/', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('admin/', admin_user, name='admin'),

    # path('', index, name='index'),
    # path('dashboard/', dashboard),
    # path('logout/', logout),
    # path('', include('social_django.urls')),
    # path('social-auth/', include('social_django.urls', namespace="social")),
]
