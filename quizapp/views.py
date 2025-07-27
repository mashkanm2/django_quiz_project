

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Book,Author,Employee,Company
from .serializers import UserSerializer,BookSerializer,EmployeeSerializer,CompanySerializer


class UserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer



class BookView(generics.ListAPIView):
    serializer_class=BookSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        queryset=Book.objects.select_related("author").all()
        return queryset 



class EmployeeView(generics.ListAPIView):
    serializer_class=EmployeeSerializer
    permission_classes = None
    def get_queryset(self):
        queryset=Employee.objects.all()
        return queryset

class CompanyView(generics.ListAPIView):
    serializer_class=CompanySerializer
    permission_classes=None
    queryset=Company.objects.all()