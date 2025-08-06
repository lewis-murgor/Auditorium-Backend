from rest_framework import permissions

class IsManagerOrReadOnly(permissions.BasePermission):
    """
    Only users with role 'manager' can create, update or delete.
    Everyone else (authenticated) can only read.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS are: GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        # Non-safe methods: POST, PUT, DELETE
        return request.user.is_authenticated and request.user.role == 'manager'
