django-template
===============

Tested on Django 1.9 and Python 3.4


Main Features
-------------

#. django-compressor

#. grappelli

#. zurb-foundation using Sass


Extra Packages
----------------

#. django-crispy-forms

#. requests

Everything configured and ready to play.


Quick usage
-----------

Start a new django project using this template::

    $ django-admin.py startproject --template=https://github.com/heigler/django-template/archive/master.zip your_project_name


Install all global packages listed on system_requirements.txt


Install all python packages (in virtualenv)::

    $ pip3.4 install -r requirements.txt


Do some extra setup using manage.py::

    $ ./manage.py migrate

    $ ./manage.py bower install

    $ ./manage.py runserver

and enjoy it
