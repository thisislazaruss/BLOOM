# forms.py
from django import forms
from .models import *
  
class breastcancerForm(forms.ModelForm):
  
    class Meta:
        model = Hotel
        fields = ['name', 'breastcancer_Main_Img']