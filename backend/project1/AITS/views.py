from rest_framework import viewsets
from .models import CustomUser, Department
from .serializers import CustomUserSerializer, DepartmentSerializer

# Create your views here.

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class DepartmentViewset(viewsets.ModelViewSet):
        queryset = Department.objects.all()
        serializer_class = DepartmentSerializer