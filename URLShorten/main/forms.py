from dataclasses import fields
from pyexpat import model
from django import forms
from .models import short_urls

class UrlForm(forms.ModelForm):
    class Meta:
        model = short_urls
        fields = ['long_url']