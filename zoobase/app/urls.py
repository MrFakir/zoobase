from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('add/', AddPage.as_view(), name='add_page'),
    # path('app/', index1),
    # path('<str:slag>/', index1),
]
