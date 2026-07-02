from rest_framework.permissions import BasePermission


class IsSelfOrAdmin(BasePermission):
    """
    Пользователь видит только себя,
    админ — всех.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # админ может всё
        if request.user.is_staff or request.user.is_superuser:
            return True

        # обычный пользователь — только свой объект
        return obj.id == request.user.id
