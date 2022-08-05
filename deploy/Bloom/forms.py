# forms.py
from django import forms
from Bloom.models import image_upload

class ImageForm(forms.ModelForm):

    class Meta:
        model = image_upload
        fields = ['image_name', 'image']

