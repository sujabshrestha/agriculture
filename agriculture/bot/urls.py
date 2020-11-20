from django.urls import path
from .views import chatbot,test

app_name = "bot"

urlpatterns = [
    path('chatbot/', chatbot,name='chatbot'),
    path('test/', test,name='test'),
]