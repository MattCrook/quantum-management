from quantummanagementapp.views.admin_users.auth.actions import login_user, logout_user, admin_user
# from quantummanagementapp.views.auth0 import dashboard, index, logout
from quantummanagementapp.views.home import landing_page, home
from django.urls import path
from django.conf.urls import include, url
from quantummanagementapp import views
from .views import *


app_name = "quantummanagementapp"

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('', include('django.contrib.auth.urls')),
    path('login/home/', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('admin/', admin_user, name='admin'),
    path('employees/', employee_list, name='employee_list'),
    path('employee/form', employee_form, name='employee_form'),
    path('employee/<int:employee_id>/form', employee_edit_form, name='employee_form'),

]

# path('', index, name='index'),
# path('dashboard/', dashboard),
# path('logout/', logout),
# path('', include('social_django.urls')),
# path('social-auth/', include('social_django.urls', namespace="social")),
