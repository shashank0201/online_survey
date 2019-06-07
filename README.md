# online_survey
Django based portal where an User can vote for his favourite multiple movies once and can see overall survey report for all the listed movies.

## Getting Started

### Setting up a Dev Environment

online_survey is a Python 2.7 application

1. On GitHub, fork the repo by clicking the Fork button in the GitHub UI.
2. Clone the repo on your local machine and go into the directory:

       $ git clone https://github.com/shashank0201/online_survey.git
       $ Run the command :from the path where manage.py exist: python manage.py runserver

3. Go to 0.0.0.0:8000/survey in your browser.


To run project:
Steps:
1. Install the required libraries through requirements.txt
2. Import the MySQL db(survey_project.sql) by following below commands:
    CREATE DATABASE newdatabase;
    mysql -u [username] -p newdatabase < survey_project.sql
    
3. Replace the database name in online_survey/survey_project/settings.py that you have set in above command (newdatabase)

* DATABASES = {
*    'default': {
*       'ENGINE': 'django.db.backends.mysql',
*        'NAME': 'newdatabase',
*        'USER': '[your system username]',
*        'PASSWORD': '[password]',
*        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
*        'PORT': '3306',
*    }
* }
