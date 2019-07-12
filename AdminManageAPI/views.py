from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse,JsonResponse
from rest_framework import viewsets, exceptions,serializers,status
from rest_framework.views import APIView
from rest_framework.filters import *
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
# Create your views here.
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from AdminManageAPI.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication,SessionAuthentication]

    permission_classes=[IsAuthenticated,IsAdminUser]

    queryset=User.objects.all()
    serializer_class = UserSerializer



class AssetViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication,SessionAuthentication]
    permission_classes=[IsAuthenticated]

    queryset=Asset.objects.all()
    serializer_class = AssetSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    
    authentication_classes=[TokenAuthentication, SessionAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]

    queryset=Worker.objects.all()
    serializer_class = WorkerSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    
    authentication_classes=[TokenAuthentication, SessionAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]

    queryset=Activity.objects.all()
    serializer_class = ActivitySerializer

class AssignTaskViewSet(APIView):
    
    authentication_classes=[TokenAuthentication, SessionAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]


    def get(self,request):
        tasks=None
        worker=self.request.query_params.get('worker')
        if worker:

            tasks= TaskAssign.objects.filter(worker=int(worker))
        else:
            tasks= TaskAssign.objects.all()
        serializer= TaskAssignSerializer(tasks,many=True)

        return Response(serializer.data,status=200)

    def post(self,request):
        data=request.data
        serializer= TaskAssignSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    
    
    
    
    
    
    
# class AssignTaskViewSet(APIView):

    
    
    
    
#     queryset=TaskAssign.objects.all()
#     serializer_class = TaskAssignSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('worker')
    # def get_queryset(self):
    #     queryset=TaskAssign.objects.all()
    #     worker_id=self.request.query_params.get('worker_id','')
    #     if worker_id:
    #         worker_id=int(worker_id)
    #         return queryset.filter(worker=worker_id)
    #     return queryset



from django.contrib.auth import login as dj_login, logout as dj_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt

class LoginView(APIView):
    @csrf_exempt
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        dj_login(request,user)
        token,created=Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=200)


class LogoutView(APIView):
    authentication_classes=(TokenAuthentication,SessionAuthentication)
    
    def post(self,request):
        dj_logout(request)
        return Response(status=204)

        

import json
def getuser(request):
    authentication_classes=(TokenAuthentication,)
    return JsonResponse({'id':request.user.id})
    