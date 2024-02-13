from rest_framework.permissions import BasePermission

class IsAuthenticatedForItemsApp(BasePermission):
    """
    Custom permission to allow access only to authenticated users for views
    within the 'items' app.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
