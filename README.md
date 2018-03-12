# tdd-test-django-rest

### clone this repository 
`https://github.com/vubon/tdd-test-django-rest.git`

### go to project directory
`cd tdd-test-django-rest`

### create virtual venv

`virtualenv -p python3 venv`

[ if error try ]
```
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"

```

### activate virtual environment
`source venv/bin/activate`



### install requirements
`pip install -r requirements.txt`



### make migration
```
python manage.py makemigrations
python manage.py migrate
```

### create superuser
`python manage.py createsuperuser`


### run server

`python manage.py runserver`
