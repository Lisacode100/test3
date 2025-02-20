from rest_framework import serializers
from .models import CustomUser, Department

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        field = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        field = '__all__'        