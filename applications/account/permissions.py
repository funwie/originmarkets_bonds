from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to read it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are only allowed to the owner of the bond.
        return obj == request.user