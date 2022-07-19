from rest_framework import serializers
from django.contrib.auth import get_user_model


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'last_login', 'is_superuser', 'username', 'first_name',
                  'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
        extra_kwargs = {
            'id': {'read_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
        }
