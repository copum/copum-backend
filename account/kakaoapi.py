import requests
import json

from config.settings import SOCIAL
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


class kakao_login(APIView) :
    def get(self, request):
       
        try :
            kakao = SOCIAL.get('kakao')
            access_token = request.GET['access_token']
            headers = {
                'Authorization' : "Bearer %s" % access_token
            }
            user_profile = requests.get(kakao.get('get_profile'), headers=headers).json()

            # 닉네임과 이메일 데이터를 가져온다.
            nickname = user_profile['kakao_account']['profile']['nickname']
            email = user_profile['kakao_account']['email']
            profile_image = user_profile["kakao_account"]['profile']['profile_image_url']
            
            # # 데이터 베이스에 이미 저장되어있는 회원이면, user에 회원 저장하기
            if User.objects.filter(email=email).exists() :
                user = User.objects.get(email=email)

            # # 회원 가입일 경우
            else :
                user = User.objects.create(
                    LOGIN_TYPE = 'kakao',
                    email=email,
                    user_id=nickname,
                    profile_image=profile_image,
                )

            user.save()

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