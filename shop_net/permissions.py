from rest_framework import permissions

class IsActiveEmployee(permissions.BasePermission):
    """
    Разрешает доступ только активным сотрудникам (is_active=True)
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.is_active  # Проверка, что сотрудник активен
        )
