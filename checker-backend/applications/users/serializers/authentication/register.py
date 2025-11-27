from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict) -> dict:
        email = attrs.get('email')

        if User.objects.filter(Q(username=email) | Q(email=email)).exists():
            raise serializers.ValidationError({'email': 'A user already exists.'})
        
        return attrs
    
    def create(self, validated_data: dict) -> User:
        email = validated_data.get('email')

        return User.objects.create_user(
            username=email,
            email=email,
            password=validated_data.get('password'),
            is_active=False,
        )
