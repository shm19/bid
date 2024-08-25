from django.urls import path
from bid.views import say_hello

urlpatterns = [
    path('hello/' , say_hello)
]
