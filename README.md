

# setup requirements
This app uses python 3.12.1 and django 6.0.1.
For the frontend, it requires node to install Vue, Quasar, js, Typescript, Axios. 
I'm using the Django Framework for ORM and using it to support an SQLite3 database. 

For development, I've been using PyCharm for the backend and Visual Studio Code for the frontend.
You'll need to activate a virtual environment first to be able to run this. 

If you're running Windows, install `python` and inside your project root directory, 
create the virtual environment folder via: `python -m venv venv`. Then activate the 
virtual environment with: `venv\Scripts\activate`

For Mac/Linux, install `python3`. Install the python3-venv package with this command:
`sudo apt install python3.13-venv` and create the virtual environment folder via: `python3 -m venv venv`.
Then activate the virtual environment with: `source venv/bin/activate`.

Install the necessary dependencies by running this command: `pip install -r requirements.txt`
Go to the frontend directory: `cd frontend` and install pnpm: `pnpm install`

In `kpi_project`, my configurations are set. You just need to create your own `settings.py` file inside and set your configurations as needed.
Most of this stuff was automatically set up when I created the Django app. However, there's a few extra details that need to be addec
since I've set up the frontend (using Quasar Framework) as an SPA served by the Django backend server.

In `kpi_project` > `settings.py`, make sure your `BASE_DIR` is set to your project root directory.
Pay special mind to `STATIC_URL` and `STATICFILES_DIRS` for setting up SPA and `DATABASES` for setting up SQLite3. (or whatever database you prefer)
```
import os
from pathlib import Path

# base directory: our root directory
BASE_DIR = Path(__file__).resolve().parent.parent 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = <some auto-generated secret key from when this Django app was first made>

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kpi_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kpi_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kpi_project.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "kpi_library.db",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "dist" / "spa",  # contains index.html, js, css
]
```

Set up database with: `python manage.py migrate`

Go to the frontend directory: `cd frontend`
Build the frontend: `pnpm run build`

You might notice that I still have the frontend dev server setup for `devServer` in `frontend` > `quasar.config.ts`. 
That's because I'm still really working on this app and when I'm developing, I run a separate frontend server
so that I can see my changes without having to rebuild my frontend every time. 
Feel free to delete that section completely if you don't need that. 

# After setting up your IDE for the app
In `management` > `commands` I have a one-time data import file called `import_classifications.py` 
where I import the GICS industry categorization references I cleaned in an Excel file that is under the folder 
`classifications`. 

In order to have the GICS industry categorizations available so you can match them to new KPI inputs that you want to add,
run this command in your project root directory once `python manage.py import_classifications`.

# industry categorization
I cleaned the Excel file manually so that it can be used as a reference for my models in `models.py` to create the structure of the database. 
This may differ based on your own needs. If you do decide to use a different industry categorization system, keep in mind that you'll need to change your models in `models.py` accordingly to match whatever system you decide to use. 

![Listing out input KPIs](screenshots/GICSexcel.png)

<p>The industry mapping is available on the GICS website: https://www.msci.com/indexes/index-resources/gics </p>
<p>The link to the original GICS 2025 Map: https://www.msci.com/documents/1296102/23c8ec04-fd1c-3518-e04c-4aa37027889d </p>

I only cleaned it enough so that it could be easily imported into the app, which meant removing superfluous notes, deleting outdated/replaced categories, and making sure codes were unique per row for each division. Nothing special. 

# running it locally
Run the Django app by going to the project root directory and running in the terminal: `python manage.py runserver`.
it should then automatically open the browser to the app. 

# how it looks currently
The app is still very much in development!

I have a simple layout for listing out GCIS industries by its sectors and subsectors.
Below this, I have a form where KPIs can be input and different details can be added to it. 

The idea is to be able to sort through different industries and their subsectors and input important KPIs related to them.
This would make it easier to keep track of which KPI is important for which sector when doing research. 

Here I've given a few examples to the KPI database. 
You can add in the description some extra information explaining what parts of the formula mean, the unit used, whether it's good if it's lower, higher or on target, as well as frequency with which we keep track of this KPI.
![Example of inputting KPIs](screenshots/frontpage.png)
![Listing out input KPIs](screenshots/kpi-cards.png)






