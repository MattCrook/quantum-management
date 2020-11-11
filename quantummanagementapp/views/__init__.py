from .home import landing_page, home
from .admin_users import admin_user, logout_user, register_user, login_user, get_admin_user_profile, admin_user_edit_form, gmail_authenticate, auth_return
from .employees import employee_list, employee_form, employee_edit_form, get_employee_details, employee_landing_page, employee_list_specific_role
from .parks import park_list, park_details, park_form, park_edit_form, park_list_employees, park_category_details_list
from .roles import role_list
from .attractions import create_attraction, attraction_type_list, delete_attraction, add_attraction_visitor
from .overview import overview, analytics
from .auth0 import Auth0
# from .admin_users import admin_user_register
