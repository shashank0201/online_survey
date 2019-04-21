# online_survey
A Online Survey portal for a User to vote for favourite movies once.

To run project:
Steps:
1. Install the required libraries through requirements.txt
2. Import the MySQL db(survey_project.sql) by following below commands:
    CREATE DATABASE newdatabase;
    mysql -u [username] -p newdatabase < survey_project.sql
    
3. Replace the database name in online_survey/survey_project/settings.py that you have set in above command (newdatabase)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newdatabase',
        'USER': '[your system username]',
        'PASSWORD': '[password]',
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
    
4. Run the command :from the path where manage.py exist> python manage.py runserver
