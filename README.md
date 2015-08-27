


How to run on command line (terminal)
-----------
1. Clone the project `git clone https://github.com/aysin/Url_Shortener`

2. For install requirement run `pip install -r requirements.txt `

3. Run `python manage.py syncdb`

4. Run `python manage.py migrate` to create the project models.

5. Run `python manage.py import_words` for import file words.txt from root of project

6. Run the development server `python manage.py runserver`

7. Visit http://127.0.0.1:8000/ to generate short url.
