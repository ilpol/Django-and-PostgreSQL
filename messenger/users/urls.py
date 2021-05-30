from django.urls import path

from . import views

urlpatterns = [
     # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<str:name>/user_hobby/', views.user_hobby, name='user_hobby'),
    path('add_users/', views.add_users, name='add_users'),
]