How to install django framework for APlus project to launch in Web Browser

- make virtual environment
$python3 -m venv myvenv

- start vertual environment
$myvenv\Scripts\activate (Windows)
$source myvenv/bin/activate (Mac OS)

- check python version and update latest
(myvenv) ~$ python3 -m pip install --upgrade pip

- install django
(myvenv) ~$ pip install django~=2.0.0

- start django project named APlus
(myvenv) ~/APlus$ django-admin startproject mysite . (Mac OS)
(myvenv) C:\Users\Name\APlus> django-admin.py startproject mysite . (Windows)

- configure database (because this is django framework.. we don't use database this time, but still need to configure)
(myvenv) ~/APlus$ python manage.py migrate

- start web server
(myvenv) ~/APlus$ python manage.py runserver

- Browser
http://127.0.0.1:8000/

- make web application named dashboard
(myvenv) ~/APlus$ python manage.py startapp dashboard
