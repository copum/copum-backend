import json
import requests
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET'])
def getData(request):
    person = { 'name':'jaechan', 'age': 26 }
    return Response(person)

@api_view(['POST'])
def getData2(request):
    person = { 'name':'asdf', 'age': 21231 }
    return Response(person)


class KakaoGetLogin(APIView) :
    def get(self, request):
        CLIENT_ID = 'f319f13f72f1e9a8b71e4971aa18d6aa'
        REDIRET_URL = "http://localhost:8000/users/kakao/login/callback/"
        url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}".format(
            CLIENT_ID, REDIRET_URL)
        res = redirect(url)
        print(res)
        return res


class getUserInfo(APIView) :
    def get(self, request):
        CODE = request.query_params['code']
        url = "https://kauth.kakao.com/oauth/token"
        res = {
            'grant_type': 'authorization_code',
            'client_id': 'f319f13f72f1e9a8b71e4971aa18d6aa',
            'redirect_url': "http://localhost:8000/users/kakao/login/callback/",
            'client_secret': 784751,
            'code': CODE
        }
        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        response = requests.post(url, data=res, headers=headers)
        # 그 이후 부분
        tokenJson = response.json()
        userUrl = "https://kapi.kakao.com/v2/user/me"  # 유저 정보 조회하는 uri
        auth = "Bearer " + tokenJson['access_token']
        HEADER = {
            "Authorization": auth,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        res = requests.get(userUrl, headers=HEADER)
        return Response(res.text)


