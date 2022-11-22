from django.contrib import admin

from .models import Produto, Lista, Mercado

admin.site.register(Lista)
admin.site.register(Mercado)
admin.site.register(Produto)

