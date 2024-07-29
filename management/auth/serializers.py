from rest_framework import serializers
import uuid
from .models import Identity
from datetime import datetime

class IdentityGoogleSerializer(serializers.Serializer):

    email = serializers.EmailField()
    uid = serializers.UUIDField(default = uuid.uuid4)
    fullName = serializers.CharField(max_length=60)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False)
    last_login_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Identity.objects.create(**validated_data)

class IdentitySerializer(serializers.Serializer):

    email = serializers.EmailField()
    uid = serializers.UUIDField(default = uuid.uuid4)
    fullName = serializers.CharField(max_length=60)
    passwordHash = serializers.CharField()
    hashSalt = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField(required=False)
    last_login_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Identity.objects.create(**validated_data)
    