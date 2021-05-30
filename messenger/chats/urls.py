from django.urls import path

from . import views

urlpatterns = [
    path('<str:messages>/<str:chat_name>/<str:users>/add_chat/', views.add_chat, name='add_chat'),
]