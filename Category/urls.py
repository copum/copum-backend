from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_main),
    path('<int:pk>', views.question_post_detail),
]