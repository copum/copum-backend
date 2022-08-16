from rest_framework.views import APIView

from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from authenticate import jwt_login, SafeJWTAuthentication, AdministratorAuthentication


User = get_user_model()

# Mixin: 사용될 모든 api view에 필요한 접근 권한에 대한 설정을 쉽게 상속할 수 있도록 미리 만들어놓은 클래스

class ApiAuthMixin:
    authentication_classes = (SafeJWTAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )

class SuperUserMixin:
    authentication_classes = (AdministratorAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PublicApiMixin:
    authentication_classes = ()
    permission_classes = ()


class GoogleLoginApi(PublicApiMixin, APIView):
    def get(self, request, *args, **kwargs):
        app_key = settings.GOOGLE_OAUTH2_CLIENT_ID
        scope = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"
        
        redirect_uri = settings.BASE_BACKEND_URL + "/account/google/login/callback"
        google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"
        
        response = redirect(
            f"{google_auth_api}?client_id={app_key}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
        )
        
        return response


class GoogleSigninCallBackApi(PublicApiMixin, APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        google_token_api = "https://oauth2.googleapis.com/token"
        
        access_token = google_get_access_token(google_token_api, code)
        user_data = google_get_user_info(access_token=access_token)
        
        profile_data = {
            'username': user_data['email'],
            'first_name': user_data.get('given_name', ''),
            'last_name': user_data.get('family_name', ''),
            'nickname': user_data.get('nickname', ''),
            'name': user_data.get('name', ''),
            'image': user_data.get('picture', None),
            'path': "google",
        }

        
        user, _ = social_user_get_or_create(**profile_data)

        response = redirect(settings.BASE_FRONTEND_URL)
        response = jwt_login(response=response, user=user)

        return response

# ***********************************************************************************

# users 이용 - 사용자의 회원가입

from django.db import transaction
from django.utils import timezone

from users.models import Profile


@transaction.atomic
def social_user_create(username, password=None, **extra_fields):
    user = User(username=username, email=username)
    
    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()
        
    user.full_clean()
    user.save()
    
    profile = Profile(user=user)
    
    try:
        profile.image = extra_fields['image']
    except:
        pass
    
    if extra_fields['nickname'] == '':
       profile.nickname = username
    else:
       profile.nickname = extra_fields['nickname']
    
    try:
        try:
            user.first_name = extra_fields['first_name']
            user.last_name = extra_fields['last_name']
        except:
            try:
                user.first_name = extra_fields['name']
            except:
                pass
    except:
        pass
    
    try:
        path = extra_fields['path']
        profile.signup_path = f"{path}"
        profile.image = f"profile_image/{path}_basic.png"
    except:
        pass
    
    profile.save()
    
    return user


@transaction.atomic
def social_user_get_or_create(username, **extra_data):
    user = User.objects.filter(email=username).first()
    
    if user:
        return user, False
    
    return social_user_create(username=username, **extra_data), True

 
# ***********************************************************************************

# google_get_access_token 함수: 구글로그인에 성공해서 받은 인증 코드(code)를 가지고 접근 토큰(access_token)을 받는 기능
# google_get_user_info 함수: access_token을 통해서 유저 정보를 가져오는 기능

import requests
from django.core.exceptions import ValidationError


GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


def google_get_access_token(google_token_api, code):
    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET
    code = code
    grant_type = 'authorization_code'
    redirection_uri = settings.BASE_BACKEND_URL + "/account/google/login/callback"
    state = "random_string"
    
    google_token_api += \
        f"?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type={grant_type}&redirect_uri={redirection_uri}&state={state}"
    
    token_response = requests.post(google_token_api)
    
    if not token_response.ok:
        raise ValidationError('google_token is invalid')
    
    access_token = token_response.json().get('access_token')
    
    return access_token


def google_get_user_info(access_token):
    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        params={
            'access_token': access_token
        }
    )

    if not user_info_response.ok:
        raise ValidationError('Failed to obtain user info from Google.')
    
    user_info = user_info_response.json()
    
    return user_info