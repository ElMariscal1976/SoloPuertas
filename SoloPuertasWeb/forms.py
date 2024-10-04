from django import forms
from django.forms import ModelForm
from SoloPuertasWeb.models import Contacto, Subscripcion

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class SubscripcionForm(ModelForm):
    class Meta:
        model = Subscripcion
        fields = '__all__'