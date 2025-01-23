## Login/ Register

![login](../quantummanagementapp/static/images/Login.png)

* A user has mmany options for a secure authentication process/ login. This project is meant to simulate users having differnt permissions for the application.
  * **Superuser** - If given superuser permissions, user will have their credentials already securely stored, so the user can simply use the login form and will have access to the Django Admin dashboard as well. 
  * **SysAdmin** - As a sysadmin user, the user may register their sysadmin account and log in through the login form as well. A SysAdmin has full access to the application with the exemption of the Django Admin dashboard.
  * **Admin User** - Regular user with basic permissions in the application. To access their account and log into the application, admin users will authenticate via one of the social login options, using their email.


![register](../quantummanagementapp/static/images/Register.png)
