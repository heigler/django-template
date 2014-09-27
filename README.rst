django-template
===============

Tested on Django 1.7 and Python 2.7


Main Features
-------------

#. django-compressor

#. zurb-foundation using Sass


Extra Packages
----------------

#. bpython

#. django-braces

#. django-floppyforms

#. coverage

#. django-debug-toolbar

#. requests

Everything configured and ready to play.


Quick usage
-----------

Start a new django project using this template::

    $ django-admin.py startproject --template=https://github.com/heigler/django-template/archive/master.zip your_project_name


Install all global packages listed on system_requirements.txt


Install all python packages (in virtualenv)::

    $ pip install -r requirements/local.txt


Do some extra setup using manage.py::

    $ ./manage.py migrate

    $ ./manage.py bower_install

    $ ./manage.py runserver

and enjoy it
