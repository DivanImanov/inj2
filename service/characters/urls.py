from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<str:character>/', views.character_page),
    # path('<str:character_name>', views.CharacterDetailView.as_view())
]