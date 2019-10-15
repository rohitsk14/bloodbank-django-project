from django import forms
from .models import requests,messages


class messageform(forms.ModelForm):
        class Meta:
            model = messages
            fields = ['name','message','email']


class requestform(forms.ModelForm):
        class Meta:
            model = requests
            fields = ['name','hospital_name','blood_group','city','mobile_no']