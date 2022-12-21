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
