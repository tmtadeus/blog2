from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home',),
    path('about/', views.about, name='about'),
    path('create_article/', views.create_article, name='createarticle'),
    path('signup/', views.signup, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:article_id>', views.detail, name='detail'),
]
