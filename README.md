# Attendence-Tracker

To run the backend on your device 

## Clone this repository

```bash
git clone https://github.com/Aaryanajith/AttendenceTracker_backend.git
```

## Install postgresql and create a table and change the name, username and password in the settings.py file

Create a new table,

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<name of the table you created>',
        'USER': '<postgresql username>',
        'PASSWORD': '<postgresql password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
now run the project.


## Install all the necessary requirements

```bash
pip install -r requirements.txt
```

## Run the backend on Local Host

```bash
python manage.py runserver
```
