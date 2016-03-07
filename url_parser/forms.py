from django import forms
from .models import UrlAdminModel


class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlAdminModel
        fields = ['url', 'timeshift', 'success']
