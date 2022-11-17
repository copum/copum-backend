from email import header
from http.client import responses
from django.shortcuts import render
from config.settings import SOCIAL
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.models import User
import requests
import json


class kakao_login(APIView) :
    def get(self, request):
        try :
            kakao = SOCIAL.get('kakao')
            access_token = request.GET['access_token']
            headers = {
                'Authorization' : "Bearer %s" % access_token
            }
            user_profile = requests.get(kakao.get('get_profile'), header=headers).json()
            print(user_profile)
            success_response = {
                'error' : False,
                'message' : '로그인 성공',
                'email' : 'test',
                'status' : 200
            }
            return Response(success_response)

        except Exception as ex :
            print('fail')
            response = {
                'error' : True,
                'message' : ex,
                'status' : 400
            }
            return Response(response)