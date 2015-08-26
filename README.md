=====
urlShortener
=====

django-url-shortener-words is a simple Django app to short urls by words library.
The shortened URLs will have the form http:// myurlshortener.com/<word>/ where <word> is a word from the english language.


Quick start
-----------
1. Clone project `git clone git@bitbucket.org:zavode/django-url-shortener-words.git`

2. For install requirement run `pip install -r requirements.txt`

3. Run `python manage.py syncdb`

4. Run `python manage.py migrate` to create the project models.

5. Run `python manage.py import_words` for import file words.txt from root of project

6. Add `HOST` value to your settings (ex: HOST = '127.0.0.1:8000')

7. Run test `python manage.py test`

8. Start the development server and visit http://127.0.0.1:8000/
   to generate short url.