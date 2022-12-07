from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from core.models import Lista, Mercado, Produto
from core.serializers import (
    ListaSerializer,
    MercadoSerializer,
    ProdutoSerializer,
    UserSerializer,
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListaViewSet(ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer


class MercadoViewSet(ModelViewSet):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
