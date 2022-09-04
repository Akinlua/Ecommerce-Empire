from django.shortcuts import render
from .models import Profile
from Market.serializers import ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from Market import custompermission

class ProfileList(generics.ListAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileSerializer
    name= 'profile-list'
    permission_classes=(
        custompermission.profileview,
    )
    

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileSerializer
    name= 'profile-detail'
    permission_classes=(
        custompermission.profileview,
    )