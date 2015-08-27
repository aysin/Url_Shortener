


How to run on command line (terminal)
-----------
1. Clone the project `git clone https://github.com/aysin/Url_Shortener`

2. Change directory 'cd Url_Shortener' 

3. Run 'sudo easy_install pip'

4. Run 'sudo easy_install Django==1.8' 

5. For install requirement run `pip install -r requirements.txt `

6. Run `python manage.py syncdb`

7. Run `python manage.py migrate` to create the project models.

8. Run `python manage.py import_words` for import file words.txt from root of project

9. Run the development server `python manage.py runserver`

10. Visit http://127.0.0.1:8000/ to generate short url.
