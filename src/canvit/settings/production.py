import os

##These settings are only suitable for production, no need to configure them if it's development
if os.environ.get('PROD'):

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['canvit.herokuapp.com']

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'django_comments_xtd',
        'django_comments',
        'id',
        'blog',
        'star_ratings',
        'home',
        'business',
        'canvit',
        'user_profile',
        'smart_selects',
        'storages'
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

    ROOT_URLCONF = 'canvit.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates/')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'canvit.context_processors.current_site',
                    'canvit.context_processors.hi'
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'canvit.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    #Heroku POSTGRESQL database settings

    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
    #DATABASES['default']['CONN_MAX_AGE'] = 500

    # Password validation
    # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/1.11/topics/i18n/

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/

    #I must set a environmental variable PROD=True, if I am on production to avoid import these settings on development

    AWS_STORAGE_BUCKET_NAME = 'canvit-bucket'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    AWS_FILE_EXPIRE = 200
    AWS_PRELOAD_METADATA = True
    AWS_QUERYSTRING_AUTH = True

    # Tell django-storages the domain to use to refer to static files.
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
    # you run `collectstatic`).
    STATICFILES_STORAGE = 'canvit.aws.utils.StaticRootS3BotoStorage'

    STATICFILES_DIRS = (
        '%s/main-static' % BASE_DIR,
    )

    DEFAULT_FILE_STORAGE = 'canvit.aws.utils.MediaRootS3BotoStorage'
    MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_ROOT = MEDIA_URL

    # Login settings
    LOGIN_REDIRECT_URL = '/home/'
    LOGIN_URL = '/accounts/login/'
    LOGOUT_REDIRECT_URL = '/home/'

    import datetime
    two_months = datetime.timedelta(days=61)
    date_two_months_later = datetime.date.today() + two_months
    expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

    AWS_HEADERS = {
         'Expires': expires,
         'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
    }

    # SSL/TLS settings
    CORS_REPLACE_HTTPS_REFERER      = True
    HOST_SCHEME                     = "https://"
    SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT             = True
    SESSION_COOKIE_SECURE           = True
    CSRF_COOKIE_SECURE              = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
    SECURE_HSTS_SECONDS             = 1000000
    SECURE_FRAME_DENY               = True

    # App settings
    SITE_ID = 1
    ACCOUNT_ACTIVATION_DAYS = 3
    COMMENTS_APP = 'django_comments_xtd'

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'canvitapp@gmail.com'
    #EMAIL_HOST_PASSWORD = 'f,krik694'
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
