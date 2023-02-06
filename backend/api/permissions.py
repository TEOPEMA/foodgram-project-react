from rest_framework.permissions import (BasePermission,
                                        IsAuthenticatedOrReadOnly)


class AuthorAdminOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in ('GET', )
            or (
                request.user.is_authenticated
                and (
                    request.user.is_superuser
                    or request.user == obj.author
                )
            )
        )


class AdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in ('GET', )
            or (
                request.user.is_authenticated
                and request.user.is_superuser
            )
        )


class AdminOwnerOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in ('GET', )
            or (
                request.user.is_authenticated
                and (
                    request.user.is_superuser
                    or request.user == obj
                )
            )
        )
