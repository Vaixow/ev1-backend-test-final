from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la lista del admin
    list_display = ("nombre", "telefono", "correo", "direccion")
    
    # Campos que se pueden buscar
    search_fields = ("nombre", "correo", "telefono")
    
    # Filtros laterales
    list_filter = ()  # si quieres, puedes filtrar por campos específicos
    
    # Orden por defecto
    ordering = ("nombre",)
    
    # Paginación
    list_per_page = 25
    
    # Campos autocompletables (si hay FK grandes)
    autocomplete_fields = ()
    
    # Acciones personalizadas
    actions = ["exportar_contactos_csv"]
    
    @admin.action(description="Exportar contactos a CSV")
    def exportar_contactos_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contactos.csv"'
        writer = csv.writer(response)
        writer.writerow(["Nombre", "Teléfono", "Correo", "Dirección"])
        for c in queryset:
            writer.writerow([c.nombre, c.telefono, c.correo, c.direccion])
        return response
