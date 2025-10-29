# ev1 backend test final
ev1 backend test final

C:\ProgramData\anaconda3\Scripts\activate.bat

crea entorno virtual
python -m venv venv


activa el .bat
venv\Scripts\activate

Crea requirements.txt

django
gunicorn
python-dotenv
psycopg2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}






.env:


user=USER 
password=PASSWORD
host=HOST
port=PORT
dbname=NAME


user=postgres.qldirfxdhhfgyrjckvuj 
password=xXMZfgbAquvAa!
host=aws-1-us-east-1.pooler.supabase.com
port=6543
dbname=postgres



python manage.py createsuperuser   (admin,admin)