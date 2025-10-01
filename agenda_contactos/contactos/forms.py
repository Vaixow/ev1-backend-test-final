from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion'] ##creamos el formulario desde el modelo creado anteriormente

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            raise forms.ValidationError("El correo electrónico no es válido.")
        return correo

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not re.match(r"^\+569\d{8}$", telefono):# Valida el formato chileno: +569 seguido de 8 dígitos, sino tira error
            raise forms.ValidationError("El teléfono debe tener 8 dígitos después del '+569'")
        return telefono