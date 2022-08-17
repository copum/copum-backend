from apiclient import discovery
import httplib2
from oauth2client import client
from ..config.settings import SOCIAL
from rest_framework.response import Response
from rest_framework.decorators import api_view

# (Receive auth_code by HTTPS POST)
# auth_code = 


# If this request does not have `X-Requested-With` header, this could be a CSRF
if not request.headers.get('X-Requested-With'):
    abort(403)


@api_view(['GET'])
def google(request):
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
        userid = credentials.id_token['sub']
        email = credentials.id_token['email']
        
    except Exception as ex:
        print("fail")
        response = { 'error':True, 'message':ex}
        return Response(response)
