from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('api/v1/stigmaslist/', StigmasAPIList.as_view()),

]
