from example_app.views import hello_rest_api
from example_app.views import hello
from django.contrib import admin
from django.urls import path

urlpatterns = [
   # ... 기존 코드 ...
   path('hello/', hello),
   path('api/hello/', hello_rest_api, name='hello_rest_api'),
]
