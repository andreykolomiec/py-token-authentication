from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if request.user and request.user.is_staff:
        #     return True
        # # Якщо метод читання (list, retrieve), то доступ дозволений
        # if request.method in SAFE_METHODS:
        #     return bool(request.user and request.user.is_authenticated)
        # return False
        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (
            request.user and request.user.is_staff
        )


class IfAuthenticatedAndCreateOrListOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated
            and view.action in ["create", "list"]
        )
