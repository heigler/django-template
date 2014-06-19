django-template
===============

### Quick usage

- Start a new django project using this template:

django_admin.py startproject --template=https://github.com/heigler/django-template your_project_name


- Install all global packages listed on system_requirements.txt


- Install all python packages (in virtualenv):

pip install -r requirements/local.txt


- Do some extra setup using manage.py:

./manage.py syncdb

./manage.py migrate

./manage.py bower_install

./manage.py runserver

and enjoy it
