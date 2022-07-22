from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and view.kwargs.get('username', None) == request.user.username)


class DenyAny(BasePermission):
    def has_permission(self, request, view):
        return False
