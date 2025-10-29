from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "correo", "direccion")  # columnas visibles en el listado
    search_fields = ("nombre", "correo", "telefono")               # campo de búsqueda rápida
    list_filter = ("correo",)                                      # filtro lateral (puedes quitarlo si no sirve)
    ordering = ("nombre",)                                         # orden por nombre
    list_per_page = 25                                             # paginación de 25 registros por página

    # Ejemplo de campo de solo lectura (puedes descomentar si lo deseas)
    # readonly_fields = ("correo",)
