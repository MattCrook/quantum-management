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
    path('register/', register_user, name='register'),
    path('admin/', admin_user, name='admin'),

    path('employees/', employee_list, name='employee_list'),
    path('employees/form/', employee_form, name='employee_form'),
    path('employees/form/<int:employee_id>/', employee_edit_form, name='employee_edit_form'),
    path('employees/<int:employee_id>/details', get_employee_details, name='employee_details'),

    path('parks', park_list, name='parks'),
    path('parks/<int:park_id>/details', park_details, name='park')
]

# path('', index, name='index'),
# path('dashboard/', dashboard),
# path('logout/', logout),
# path('', include('social_django.urls')),
# path('social-auth/', include('social_django.urls', namespace="social")),
