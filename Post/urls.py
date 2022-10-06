from django.urls import path
from . import views



urlpatterns = [
    path('', views.question_post),
    path('<int:pk>', views.question_post_detail),

]