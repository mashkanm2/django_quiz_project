
from django.db import transaction,IntegrityError
from rest_framework import serializers
from .models import AuthUser,Profile,Book,Author,Company,Employee


class UserSerializer(serializers.ModelSerializer):
    class Mata:
        model=AuthUser
        fields=['username','email','password']
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self,validated_data):
        try:
            with transaction.atomic():
                user = AuthUser.objects.create(**validated_data)
                profile=Profile.objects.create(user=user,bio='')
                return user
        except IntegrityError as e:
            raise serializers.ValidationError({'error':str(e)})
        except Exception as ex:
            raise serializers.ValidationError({'error':str(ex)})




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"
    

class BookSerializer(serializers.ModelSerializer):
    author=AuthorSerializer()
    class Meta:
        model=Book
        fields=['title','author']

class EmployeeSerializer(serializers.ModelSerializer):
    company=serializers.CharField(source='company.name',read_only=True)
    class Meta:
        model=Employee
        fields=['name','company']

class CompanySerializer(serializers.ModelSerializer):
    employees=serializers.StringRelatedField(many=True)
    class Meta:
        model=Company
        fields=['name','employees']