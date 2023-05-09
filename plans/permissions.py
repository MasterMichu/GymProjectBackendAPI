from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.owner)
        print(request.user)
        print(obj.owner == request.user)
        return obj.owner == request.user

