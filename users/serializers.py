from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

    def validate_role(self, value):
        request = self.context['request']
        user = request.user

        # если не админ — запрещаем менять role
        if not user.is_staff and not user.is_superuser:
            if self.instance and self.instance.role != value:
                raise serializers.ValidationError("Нельзя менять role")

        return value
