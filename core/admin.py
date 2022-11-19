from django.contrib import admin

from .models import Produto, Lista, Mercado, Perfil

admin.site.register(Lista)
admin.site.register(Mercado)
admin.site.register(Produto)
admin.site.register(Perfil)
