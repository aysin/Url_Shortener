


How to run on command line (terminal)
-----------
1. Clone the project `git clone https://github.com/aysin/Url_Shortener`

2. Change directory 'cd Url_Shortener' 

3. Run 'sudo easy_install pip'

4. Run 'sudo easy_install Django==1.8' 

5. Run `python manage.py syncdb`

6. Run `python manage.py migrate` to create the project models.

7. Run `python manage.py import_words` for import file words.txt from root of project

8. Run the development server `python manage.py runserver`

9. Visit http://127.0.0.1:8000/ to generate short url.
