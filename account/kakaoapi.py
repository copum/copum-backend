from email import header
from http.client import responses
from django.shortcuts import render
from ..config.settings import SOCIAL
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

@api_view(['GET'])
def kakao(request):
    try:
        if(not request.GET["code"]):
            return Response({'error': True, 'message':'code를 찾을 수 없습니다.'})

        code = request.GET['code']

        headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

        data = {
            'grant_type': SOCIAL.kakao.grant_type,
            'client_id':SOCIAL.kakao.client_id,
            'redirect_uri': SOCIAL.kakao.redirect_uri,
            'code': code
        }
        user_token = requests.post(SOCIAL.kakao.get_token, data=data, headers=headers)

        token_json = user_token.json()

        if(not token_json["access_token"]):
            return Response({'error': True, 'message':'access_token을 찾을 수 없습니다.'})
        
        access_token = token_json["access_token"]

        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
            'Authorization': f"Bearer {access_token}"
        }
        
        data = { 'property_keys': '["kakao_account.email"]'}
        user_profile = requests.post(SOCIAL.kakao.get_profile, data=data, headers=headers).json()
        
        if(not user_profile["kakao_account"] or not user_profile["kakao_account"]["email"]):
            return Response({'error': True, 'message':'이메일 수집에 동의해주세요.'})

        user_email = user_profile["kakao_account"]["email"]
        findUser = User.objects.get(email=user_email)
        if(not findUser):
            return Response({'error':True, 'message': '존재하지 않는 아이디입니다. 회원가입하고 다시 시도해주세요.'})
            
        success_response = {'error':False, 'message': '로그인에 성공하셨습니다.', 'email': "test"}
        return Response(success_response)
    except Exception as ex:
        print("fail")
        response = { 'error':True, 'message':ex}
        return Response(response)

