from django import forms
from .models import appVariety

class AppVarietyForm(forms.Form):
    app_variety = forms.ModelChoiceField(queryset=appVariety.objects.all(), label="Select App Variety")