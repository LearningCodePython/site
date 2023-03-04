from django import forms
from .models import sitios


class sitios_form(forms.ModelForm):
    class Meta:
        model = sitios
        fields = '__all__'