from rest_framework import serializers,exceptions
from AdminManageAPI.models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class AssetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Asset
        fields=(
            'id',
            'name',
            'tag',
            'created_on',
            'updated_on',
            
        )


class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Activity
        fields=(
            'id',
            'name',
            'frequency',
            'created_on',
            'updated_on',
            'asset',
            
        )

class WorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Worker
        fields=(
            'id',
            'name',
            'skills',
            'phone',
            'created_on',
            'updated_on',
            
        )


class TaskAssignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TaskAssign
        fields=(
            'id',
            'task',
            'asset',
            'worker',
            'timeOfAllocation',
            'timeToComplete',
            
        )




class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get('username',"")
        password=data.get('password',"")

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                data['user']=user
            else:
                m="unable to login, wrong credential"
                raise exceptions.ValidationError(m)
        else:
            m="enter both username and password "
            raise exceptions.ValidationError(m)
        return data