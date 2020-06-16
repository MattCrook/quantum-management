def process_roles(details, user, **kwargs):
    if details['role'] == 'admin':
        user.is_staff = True
        user.is_superuser = True
        user.save()
