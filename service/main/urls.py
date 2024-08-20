from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('addpost/', views.AddPost.as_view(), name='addpost'),
    path('about/', views.about),
    path('login/', views.LoginUser.as_view()),
    path('logout/', views.logout_user)
    # path('help-the-project', views.help) # Template was removed
]