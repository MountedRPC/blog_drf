from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationsUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'repeat_password', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use")
        return value

    def create(self, validated_data):
        validated_data.pop('repeat_password', None)
        user = User.objects.create_user(**validated_data)
        return user
