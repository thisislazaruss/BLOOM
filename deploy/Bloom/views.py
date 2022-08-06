# Create your views here.
from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import tensorflow as tf

# from django.core.files.storage import FileSystemStorage

# Create your views here.


def success(request):
    loaded_model = tf.keras.models.load_model("templates/prekshyaandsrishti.h5")
    loaded_model.build(256)
    return render(request, 'success.html')


def image_upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})
