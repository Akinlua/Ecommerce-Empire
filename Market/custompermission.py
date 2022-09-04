from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS: 
            # The method is a safe method 
            return True 
        else:
            # The method isn't a safe method 
            # Only owners are granted permissions for unsafe methods 
            return obj.owner == request.user

class profileview(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS: 
            # The method is a safe method 
            return True 
        else:
            # The method isn't a safe method 
            # Only owners are granted permissions for unsafe methods 
            return obj.user.username == request.user.username

class Isowner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            if request.user.is_authenticated:
                return False
            else:
                return obj.owner.username == request.user.username

