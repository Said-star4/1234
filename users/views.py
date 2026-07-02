from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from .permissions import IsSelfOrAdmin


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrAdmin]

    def get_queryset(self):
        user = self.request.user

        # админ видит всех
        if user.is_staff or user.is_superuser:
            return User.objects.all()

        # обычный пользователь — только себя
        return User.objects.filter(id=user.id)
