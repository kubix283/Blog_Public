from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'POST', 'OPTIONS']:
            return True
        return obj.author == request.user
    

class IsOwnerAndAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser and obj.author == request.user
            