from apiclient import discovery
import httplib2
from oauth2client import client
from ..config.settings import SOCIAL
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User


# (Receive auth_code by HTTPS POST)
auth_code = ''
"""
Google api json
{"web":{"client_id":"351504897374-tjt8g2an0kio669d448sn8dec6fk31jh.apps.googleusercontent.com",
"project_id":"copum-359506",
"auth_uri":"https://accounts.google.com/o/oauth2/auth",
"token_uri":"https://oauth2.googleapis.com/token",
"auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
"redirect_uris":["http://localhost:3000/account/google/callback","http://localhost:8000/complete/google-oauth2/","http://localhost:8000/account/google/login/"],
"javascript_origins":["http://localhost:8000","http://localhost:3000"]
}
}
"""


@api_view(['GET'])
def google_login(request):
    try:
        if(not request.GET["code"]):
            return Response({'error': True, 'message':'code를 찾을 수 없습니다.'})

        code = request.GET['code']

        headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

        # Set path to the Web application client_secret_*.json file you downloaded
        CLIENT_SECRET_FILE= {
        "web":{"client_id": SOCIAL.google.client_id,
                "project_id":SOCIAL.google.project_id,
                "auth_uri":"https://accounts.google.com/o/oauth2/auth",
                "token_uri":"https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
                "javascript_origins":["http://localhost:8000","http://localhost:3000","http://copum.login.com"]
            }
        }

        # Exchange auth code for access token, refresh token, and ID token
        credentials = client.credentials_from_clientsecrets_and_code(
        CLIENT_SECRET_FILE,
        ['https://www.googleapis.com/auth/drive.appdata', 'profile', 'email'],
        auth_code)

        # Call Google API
        http_auth = credentials.authorize(httplib2.Http())
        drive_service = discovery.build('drive', 'v3', http=http_auth)
        appfolder = drive_service.files().get(fileId='appfolder').execute()

        # Get profile info from ID token
        user_id = credentials.id_token['sub']
        user_email = credentials.id_token['email']
        
        findUser = User.objects.get(email=user_email)
        if(not findUser):
            return Response({'error':True, 'message': '존재하지 않는 아이디입니다. 회원가입하고 다시 시도해주세요.'})
            
        success_response = {'error':False, 'message': '로그인에 성공하셨습니다.', 'email': "test"}
        return Response(success_response)
        
    except Exception as ex:
        print("fail")
        response = { 'error':True, 'message':ex}
        return Response(response)
