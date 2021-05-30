from django.urls import path

from . import views

urlpatterns = [
    path('<str:message_text>/<str:chat_name>/<str:user>/add_message/', views.add_message, name='add_message'),
]