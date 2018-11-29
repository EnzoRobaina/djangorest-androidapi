from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from androidapi.api import models, serializers
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class Index(APIView):
    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)

    def get(self, request, format=None):
        if request.user.status == 0:
            mensagem = 'Aguardando autorização do administrador.'
        elif request.user.status == 1:
            mensagem = 'Bem vindo.'
        else:
            mensagem = 'Você está proibido de acessar.'

        objeto = {'mensagem': mensagem, 'status': request.user.status}
        return Response(objeto)

class UsuarioViewSet(viewsets.ModelViewSet, APIView):
    """
    API endpoint para Usuario
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    queryset = models.Usuario.objects.all().order_by('-date_joined')
    serializer_class = serializers.UsuarioSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Usuario.objects.all()

        return models.Usuario.objects.all().filter(pk=self.request.user.id)

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            raise PermissionDenied()

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        perms = ['is_superuser']
        if not self.request.user.is_superuser:
            if any(perm in request.data for perm in perms):
                raise PermissionDenied()

        return super().update(request, *args, **kwargs)