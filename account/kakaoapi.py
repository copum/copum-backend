import requests
import json
from django.contrib.auth import authenticate

from config.settings import SOCIAL
from django.db.migrations import serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import render, get_object_or_404

from users.models import User
from users.serializers import UserSerializer


class kakao_login(APIView) :
    def get(self, request):
        try :
            kakao = SOCIAL.get('kakao')
            access_token = request.GET['access_token']
            headers = {
                'Authorization' : "Bearer %s" % access_token
            }
            user_profile = requests.get(kakao.get('get_profile'), headers=headers).json()
            
            if user_profile["kakao_account"]['profile']['profile_image_url'] is None:
                user_profile["kakao_account"]['profile']['profile_image_url'] = " "
            # 닉네임과 이메일 데이터를 가져온다.
            nickname = user_profile['kakao_account']['profile']['nickname']
            email = user_profile['kakao_account']['email']
            profile_image = user_profile["kakao_account"]['profile']['profile_image_url']

            data = {
                "user_id": nickname,
                "email":email,
                "profile_image": profile_image
            }
            
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email = email)
                print('1')
                print(user.id)
            else :
                serializer = UserSerializer(data=data)
                print('2')
                if serializer.is_valid():
                    user = serializer.save()
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            print(user)

            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = JsonResponse(
                {
                    "user": {"email": user.email,
                    "profile" : user.user_id,
                    "profile_image": user.profile_image                    },
                    "message": "register successs",
                    "error": False,
                    "status":200,
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
                
            )
            print(res)
            return res

        except Exception as ex :
            print('fail')
            response = {
                'error' : True,
            }
            return JsonResponse(response, status=400)