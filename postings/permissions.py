from rest_framework import permissions


# permission to allow only creators to edit the object.

class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.creator == request.user
    
    