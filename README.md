# Quantum Management

Quantum Management is a theme park management and business analysis management application built with Python/ Django. The purpose of this application is to track employees at the park, where they work, allow for addition, removal, or transition to a different role. It Only allows an admin (*HR, Management, etc...*) user to log in and have an account, and edit the employees resource to which they entered. In addition, Quantum Management provides a dashboard of analytical business intelligence information for educated business decisions, reporting, and forecasting. The information displayed is business operations and intelligence statistics like number of visitors in the park, most popular time of year, most popular rides, ride wait times, and much more customizable queries to derive financial and income tracking data. All of which are displayed using data visualization tools for easy readability and analysis.

## Project Set Up
If you wish to clone this repository to run it locally, follow these steps:

#### Run Locally Just Using Django and CLI:

* `git clone git@github.com:MattCrook/quantum-management.git`
* `cd` into the directory it creates
* `python3 -m venv venv`
* `source ./venv/bin/activate`
* `pip3 install -r requirements.txt`
* `python3 -m pip install Pillow`
* `python3 manage.py makemigrations`
* `python3 manage.py migrate`
* `python3 manage.py runserver`
* Navigate to `localhost:8000`

*(may also need to run (optional)):*
`python3 manage.py createsuperuser`
`python3 manage.py loaddata */fixtures/*.json`

#### Run With Docker
*Download Docker if not done so already*
<!-- * `docker build -t application:latest .`
* `docker run -it -d -p 8000:8000 application` -->
* `docker build -t quantummanagement .`
* `docker run -it -d --env-file .env.dev -p 8000:8000 quantummanagement`

#### Run With Docker-Compose
* `docker compose up --build`

Note - all of these options to run locally comes with/ runs a Sqlite3 Database with it for its backend database. There is also an option to run PostgresSQL, however will need to change some ENV variables and settings, as well as a couple things in the docker-compose file.

#### Run Locally with Makefile
* `make prep`
* `make venv_activate`
* `make install`
* `make venv_migrate`
* `make run_local`


#### Run Locally with PipEnv
1. Create a `.env` file.
2. pipenv install
3. pipenv sync --dev
4. pipenv run python3 install -r requirements.txt
5. pipenv run python3 -m pip install Pillow
6. pipenv run python3 manage.py makemigrations
7. pipenv run python3 manage.py migrate
8. pipenv run python3 manage.py runserver


#### Running In Different Environments

*TBD*

#### Deployment

*TBD*

<br>


## Technology Used
1. Django
2. Python
3. *SQLite*
4. Now Migrated to a **PostgreSQL** Database
5. Fixtures
6. Django ORM & SQL queries
7. Models
9. Name spacing using Django router
10. Function based views to have more control over abstraction. 
11. Class based views for API in which client side utilizes mainly for data visualizations.
12. Testing with unittest and PyTest.
13. User authentication and authorization
14. URL routing using Name Spacing
15. Docker
16. Docker Compose
17. Ngnix
18. JWT Token Based Authentication

<br>


## Quantum Management

###### *Note: this was a coding bootcamp final capstone project. While this application has many features, much of it is still slightly incomplete. Important to note as well this was created essentially as quickly as possible with an ambitious turn around time (part of the challenge in the final capstone).*

<br>


![new_homepage](./docs/images/new_homepage.png)

<br>

Quantum Management is a management and data analytics application that allows a logged in admin user to do the following:

* ##### [Home Page](./docs/home.md)
* ##### [Login/ Register](./docs/login_register.md)
* ##### [Account](./docs/account.md)
* ##### [Manage Employees](./docs/employees.md)
* ##### [Manage Park(s)](./docs/parks.md)
* ##### *Analytics*
  * [Analytics Overview](./docs/analytics_overview.md)
  * [Park Analytics](./docs/park_analytics.md)
    * Attraction Visitors
    * Park Attendance
    * Ride Wait Times
* ##### [Django Admin Dashboard](./docs/django_admin.md)

<br>


<!-- 
## Entity Relationship Diagram (ERD)
![QuantumManagementERD](quantummanagementapp/static/images/QuantumManagementERD.png)


## Wireframe 
* Basic stucture/ layout of the application's pages and dataflow.

![QuantumManagementWireframe](quantummanagementapp/static/images/QuantumManagementWireframe.png) -->
