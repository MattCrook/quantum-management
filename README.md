# Quantum Management
Quantum Management is a theme park management and business analysis management application built with Python/ Django. The purpose of this application is to track employees at the park, where they work, allow for addition, removal, or transition to a different role. It Only allows an admin (*HR, Management, etc...*) user to log in and have an account, and edit the employees resource to which they entered. In addition, Quantum Management provides a dashboard of analytical business intelligence information for educated business decisions, reporting, and forecasting. The information displayed is business operations and intelligence statistics like number of visitors in the park, most popular time of year, most popular rides, ride wait times, and much more customizable queries to derive financial and income tracking data. All of which are displayed using data visualization tools for easy readability and analysis.

## Project Set Up
If you wish to clone this repository to run it locally, follow these steps:

* `git clone git@github.com:MattCrook/quantum-management.git`
* `cd` into the directory it creates
* `python -m venv QuantumManagementEnv`
* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py runserver`


## Technology Used
1. Django
2. Python
3. SQLite
4. Fixtures
5. ORM & SQL queries
6. Models
7. Name spacing using Django router
8. Function based views to have more control over abstraction 
9. Testing with unittest
10. User authentication and authorization
11. url routing

# What Does Quantum Management Offer?
Quantum Management is a management and data analytics application that allows a logged in admin user to do the following:

## Home Page

![Home](quantummanagementapp/static/images/home.png)


## Login/ Register

![login](quantummanagementapp/static/images/Login.png)  ![register](quantummanagementapp/static/images/Register.png)

## Account


Once given credentials and logged in, an admin user may set up their account profile where they will see and be able to edit their personal information including profile picture, username, first and last name, employees assigned to them and they manage, etc...

![accountpicture](quantummanagementapp/static/images/account.png)

## Manage Employees


Admin user can see a full list of employees categorized by which department they work in.
  * Admin user can add (hire) a new employee.
  * Can edit/ delete an existing employee. However, only if the current authenticated admin user originally added that employee.
  * Can see details of a specific employee. For example which attraction they are assigned to, their wage, start date ect...
  
  ![manageemployees](quantummanagementapp/static/images/manageEmployees.png)

## Manage Park

Admin user can see a full list of parks that are currently owned/ under the organization for which they are employed.

  * Admin user can add a new park, or edit an existing one.
  * By navigating to a specific park, admin user is brought to a dashboard with many options including:
    * Park details
      * Attractions in park, categorized by *attraction type*
      * Which employees work on that attraction
      * Details and specs for that specific attraction
      * ![parkDetails](quantummanagementapp/static/images/parkdetailsdashboard.png)
    * Employees
      * Admin user can easily read list of employees that work at the current park.
      * ![employeesInPark](quantummanagementapp/static/images/employeesInPark.png)
    * Add Attraction
      * Admin user can add a new attraction (and *attraction type*) to the current park.
      * ![addAttractionForm](quantummanagementapp/static/images/AddAttraction.png)

## Park analytics

Data analysis information for creating data visualizations for business operations and intelligence.

**Coming Soon!**


## Entity Relationship Diagram (ERD)
![QuantumManagementERD](quantummanagementapp/static/images/QuantumManagementERD.png)


## Wireframe 
* Basic stucture/ layout of the application's pages and dataflow.

![QuantumManagementWireframe](quantummanagementapp/static/images/QuantumManagementWireframe.png)
