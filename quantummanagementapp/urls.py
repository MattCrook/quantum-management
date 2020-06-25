from quantummanagementapp.views.home import landing_page, home
from django.urls import path
from django.conf.urls import include, url
from quantummanagementapp import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = "quantummanagementapp"

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('', include('django.contrib.auth.urls')),

    path('login/home/', home, name='home'),
    path('login/', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('admin/', admin_user, name='admin'),

    path('account/<int:user_id>/', get_admin_user_profile, name='account'),
    path('account/<int:user_id>/form', admin_user_edit_form, name="admin_user_edit_form"),

    path('employees/', employee_list, name='employee_list'),
    path('employees/form/', employee_form, name='employee_form'),
    path('employees/form/<int:employee_id>/', employee_edit_form, name='employee_edit_form'),
    path('employees/<int:employee_id>/details', get_employee_details, name='employee_details'),

    path('parks', park_list, name='parks'),
    path('parks/<int:park_id>/details', park_details, name='park'),
    path('parks/form', park_form, name='park_form'),
    path('parks/form/<int:park_id>/', park_edit_form, name='park_edit_form')
]



+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path('', include('social_django.urls')),
# path('social-auth/', include('social_django.urls', namespace="social")),
