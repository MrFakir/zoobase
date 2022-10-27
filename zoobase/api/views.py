from django.shortcuts import render
from rest_framework import generics

from .serializers import StigmasSerializer
from app.models import Stigmas


class StigmasAPIList(generics.ListCreateAPIView):
    queryset = Stigmas.objects.all()
    serializer_class = StigmasSerializer
    permission_classes = ()

