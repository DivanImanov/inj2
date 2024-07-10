from django.urls import path, re_path
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index),
    path('<str:character>/', views.character_page),
    # path('<str:character_name>', views.CharacterDetailView.as_view())
    path('api/v1/movelist/', views.MoveListAPIView.as_view()),
    # path('api/v1/movelist/<str:name>', views.MoveListAPIView.as_view()),
]