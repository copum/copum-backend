from email import header
from http.client import responses
from django.shortcuts import render
from config.settings import SOCIAL
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
import requests
import json


# Create your views here.

"""
문서
https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api

client -> server
body
{
    code : "code..."
}
server -> kakao 인증서버
GET /oauth/authorize?client_id=${REST_API_KEY}&redirect_uri=${REDIRECT_URI}&response_type=code HTTP/1.1
Host: kauth.kakao.com
{
    "access_token": "~~~",
    "token_type": "bearer",
    "refresh_token": "~~",
    "id_token": "~~",
    "expires_in": 21599,
    "scope": "account_email openid",
    "refresh_token_expires_in": 5183999
}
"""

@api_view(['GET'])
def kakao_login(request):
    try:
        kakao = SOCIAL.get('kakao')
        access_token = request.GET["access_token"]
        headers = {
            'Authorization': "Bearer %s" % access_token
        }
        user_profile = requests.get(kakao.get('get_profile'),headers=headers).json()
        print(user_profile)
        #if(not user_profile["kakao_account"] or not user_profile["kakao_account"]["email"]):
        #    return Response({'error': True, 'message':'이메일 수집에 동의해주세요.'})

        #user_email = user_profile["kakao_account"]["email"]
        #findUser = User.objects.get(email=user_email)
        #if not findUser :
        #    return Response({'error':True, 'message': '존재하지 않는 아이디입니다. 회원가입하고 다시 시도해주세요.', 'status':401})
        ##주석
        success_response = {'error':False, 'message': '로그인에 성공하셨습니다.', 'email': "test", 'status':200}
        return Response(success_response)
    except Exception as ex:
        print("fail")
        response = { 'error':True, 'message':ex}
        return Response(response)
