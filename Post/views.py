from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Posts
from .serializers import PostSerializer

from rest_framework import generics
from .models import Question, Answer
from .serializers import QuestionListSerializer, QuestionCreateSerializer, QuestionSerializer


@csrf_exempt
def question_post(request):
    if request.method == 'GET':
        query_set = Posts.objects.all()
        serializer = PostSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    


@csrf_exempt
def question_post_detail(request,pk):
    obj = Posts.objects.get(pk = pk)

    if request.method =='GET':
        serializer = PostSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(obj, data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.error, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

# -------------------------------------------------------------
# 은배 코드 추가

class QuestionList(generics.ListAPIView) :
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionCreate(generics.CreateAPIView) :
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer


class QuestionMotion(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer