import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'USER': env('DATABASE_USER'),
        'NAME': env('DATABASE_NAME'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
        'OPTIONS': {'charset': env('DATABASE_CHARSET')}
    }
}

SECRET_KEY = env('SECRET_KEY')

SOCIAL = {
    'kakao': {
        'client_id': env('KAKAO_LOGIN_CLIENT_ID'),
        'secret': env('KAKAO_LOGIN_CLIENT_ID'),
        'key': '',
        'get_token':'https://kauth.kakao.com/oauth/token',
        'get_profile': 'https://kapi.kakao.com/v2/user/me',
        'redirect_uri': 'http://localhost:3000/kakao',
        'grant_type':'authorization_code'
    }, 
    # 'google': {
    #     'client_id': env('GOOGLE_LOGIN_CLIENT_ID'),
    #     'project_id': env('GOOGLE_PROJECT_ID'),
    #     'secret': env('GOOGLE_LOGIN_CLIENT_SECRET'),
    #     'key': '',
    #     "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    #     'get_token':"https://oauth2.googleapis.com/token",
    #     'get_profi
    # le':"https://www.googleapis.com/oauth2/v3/userinfo",
    #     'grant_type':'authorization_code'
    # }
}
