# Create your views here.
from cgitb import text
from dataclasses import dataclass
from email.mime import image
from tkinter.tix import IMAGE
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from deploy import settings
import os
# from django.core.files.storage import FileSystemStorage

# Create your views here.

INPUT_SIZE = (256, 256)

def success(request):
    loaded_model = tf.keras.models.load_model("templates/prekshyaandsrishti.h5")
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path)
    context = {"images": img_list}
    img = Image.open(path + "/" + context['images'][0])
    image = np.asarray(img)
    # print(image)
    image = tf.image.resize(image, (256,256))
    image_tensor = tf.convert_to_tensor(image, dtype=tf.float32)
    image_tensor = tf.expand_dims(image_tensor, 0)
    #image = np.array(image)
    #image= image.resize((64,64))
    #image = tf.reshape(image, shape=(3, 256,256, 3))
    
    prediction = loaded_model.__call__(image_tensor)
    return render(request, 'success.html', {})


def image_upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})