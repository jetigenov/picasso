# Picasso Soft

### Installation
1. clone repository `git@github.com:jetigenov/picasso.git`
2. create virtualenv with python3.7 `virtualenv venv`
3. install postgres 13 `brew install postgresql@13`
    - psql postgres
    - create database picasso;
4. install requirements `pip install -r requirements.txt`
5. make migrations
    - `python manage.py makemigrations`
    - `python manage.py migrate`
6. runserver
    - `python db_manage.py runserver`


##### List of calls (REQUEST METHOD: GET)
- URL: `{{base_url}}/calls` with pagination by 25
