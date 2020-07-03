from rest_framework import serializers
from .models import BlogUser


class BlogUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    emailId = serializers.CharField(max_length=100)
    contact = serializers.CharField(max_length=50)

    def create(self, validate_data):
        return BlogUser.objects.create(**validate_data)