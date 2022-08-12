from http.client import responses
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
import requests
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


CLIENT_ID = 'f319f13f72f1e9a8b71e4971aa18d6aa'
KAKAO_GET_TOKEN_URI = 'https://kauth.kakao.com/oauth/token'
GRANT_TYPE = 'authorization_code'
REDIRECT_URI = 'http://localhost:3000/kakao'
KAKAO_GET_PROFILE_URI = 'https://kapi.kakao.com/v2/user/me'
@api_view(['GET'])
def test(request):
    try:
        if(not request.GET["code"]):
            return Response({'error': True, 'message':'code를 찾을 수 없습니다.'})

        code = request.GET['code']
        print("code", code)
        headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

        data = {
            'grant_type': GRANT_TYPE,
            'client_id':CLIENT_ID,
            'redirect_uri': 'http://localhost:3000/kakao',
            'code': code
        }
        user_token = requests.post(KAKAO_GET_TOKEN_URI, data=data, headers=headers)

        token_json = user_token.json()
        
        success_response = {'error':False, 'message': '로그인에 성공하셨습니다.', 'email': 'findUser.email'}
        return Response(success_response)
    except Exception as ex:
        print("fail")
        response = { 'error':True, 'message':ex}
        return Response(response)
