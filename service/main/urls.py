from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    # path('help-the-project', views.help) # Template was removed
]