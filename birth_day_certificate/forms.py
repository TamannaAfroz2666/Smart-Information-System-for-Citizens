from django import forms
from .models import *


class BirthDayCertificateForm(forms.ModelForm):
    class Meta:
        model = BirthDayCertificate
        fields = '__all__'

