from rest_framework import serializers
from androidapi.api import models
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

class UsuarioSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data.keys():
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

    class Meta:
        model = models.Usuario
        fields = ('__all__')