#Any userr being able to edit others is unacceptable

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    #when trying to change an object the below code gets called
    def has_object_permission(self, request, view, obj):
        """get http would be a safe method because its ok to view others"""
        if request.method in permissions.SAFE_METHODS:
            return True
        #only if the equation below is true u will be able to update profile
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id