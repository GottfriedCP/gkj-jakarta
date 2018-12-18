from django import forms
from .models import Warta

class WartaForm(forms.ModelForm):
    class Meta:
        model = Warta
        fields = ['warta']
