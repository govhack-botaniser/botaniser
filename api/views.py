from django.shortcuts import render

from django.contrib.auth.models import User
from core.models import Species, Report
from rest_framework import viewsets
from api.serializers import UserSerializer, SpeciesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


# Create your views here.