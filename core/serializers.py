from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Lista, Mercado, Produto, Perfil

class ListaSerializer(ModelSerializer):
    class Meta:
        model = Lista
        fields = "__all__"

class MercadoSerializer(ModelSerializer):
    class Meta:
        model = Mercado
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        
class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        fields = "__all__"