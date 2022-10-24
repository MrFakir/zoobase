from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('add/', AddPage.as_view(), name='add_page'),
    path('accounts/login/', LoginUser.as_view(), name='login'),
    path('accounts/logout/', logout_user, name='logout'),
    path('accounts/profile/<str:slug>/password', ProfileUserPass.as_view(), name='password'),
    path('accounts/profile/<str:slug>', ProfileUser.as_view(), name='profile'),

]
