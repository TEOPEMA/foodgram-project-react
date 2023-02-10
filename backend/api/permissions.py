from rest_framework import permissions


class AuthorAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): 
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    request.user.is_superuser
                    or request.user == obj.author
                )
            )
        )


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and request.user.is_superuser
            )
        )


class AdminOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    request.user.is_superuser
                    or request.user == obj
                )
            )
        )
