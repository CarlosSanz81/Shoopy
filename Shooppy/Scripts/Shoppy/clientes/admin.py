from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'email', 'direccion',)
	list_filter = ('nombre',)
