from django.urls import path
from . import views

from .views import QuestionList, QuestionCreate, QuestionMotion

urlpatterns = [
    path('', views.question_post),
    path('<int:pk>', views.question_post_detail),

    # 은배 : Question 모델 이용
    path('question/', QuestionList.as_view()),
    path('question/create/', QuestionCreate.as_view()),
    path('question/<int:pk>/', QuestionMotion.as_view()),
]