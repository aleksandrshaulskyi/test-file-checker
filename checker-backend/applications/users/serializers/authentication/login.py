from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """
    This serializer is used to check the validity of the input.
    """

    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs: dict) -> dict:
        """
        Validate the credentials and store an instance of authenticated User
        to the serializer context.
        """
        user = authenticate(
            username=attrs.get('email'),
            password=attrs.get('password'),
        )

        if user is None:
            raise serializers.ValidationError('Invalid credentials.')
        
        if not user.is_active:
            raise serializers.ValidationError('Your account is not activated.')
        
        self.context.update({'user': user})

        return attrs
