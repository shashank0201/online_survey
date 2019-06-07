# Online Survey
Django based portal where an User can vote for his favourite multiple movies once and can see overall survey report for all the listed movies.

## Getting Started

### Setting up a Dev Environment

1. On GitHub, fork the repo by clicking the Fork button in the GitHub UI.
2. Clone the repo on your local machine and go into the directory:

       $ git clone https://github.com/shashank0201/online_survey.git
       $ cd online_survey
       $ python manage.py runserver

3. Go to 0.0.0.0:8000/survey in your browser.


Database set up(to import db in local system):
* Steps:
1. Install the required libraries through requirements.txt
2. Import the MySQL db(survey_project.sql) by following below commands:

       CREATE DATABASE NewDatabaseName;
       mysql -u [username] -p [NewDatabaseName] < survey_project.sql
    
3. Replace the database name in survey_project/settings.py that you have set in above command (NewDatabaseName)

       DATABASES = {
           'default': {
              'ENGINE': 'django.db.backends.mysql',
               'NAME': 'newdatabase',
               'USER': '[db_username]',
               'PASSWORD': '[password]',
               'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
               'PORT': '3306',
           }
       }
