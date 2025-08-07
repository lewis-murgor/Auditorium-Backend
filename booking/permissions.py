from rest_framework import permissions

class IsSpectator(permissions.BasePermission):
    """
    Allows access only to users with role 'spectator'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'spectator'


class IsBookingOwner(permissions.BasePermission):
    """
    Only allow the spectator who made the booking to cancel it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.spectator == request.user
    
class IsSalespersonOrManager(permissions.BasePermission):
    """
    Only users with role 'salesperson' or 'manager' can create or edit seats.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role in ['salesperson', 'manager']
        )