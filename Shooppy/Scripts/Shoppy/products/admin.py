from django.contrib import admin
from .models import Product, Favorito


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'precio',)
    list_filter = ('nombre', 'categoria',)


@admin.register(Favorito)
class AdminFavorito(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
