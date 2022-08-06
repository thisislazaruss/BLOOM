# Create your views here.
from cgitb import text
from dataclasses import dataclass
from email.mime import image
from tkinter.tix import IMAGE
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import tensorflow as tf
<<<<<<< HEAD
import h5py

=======
import numpy as np
from PIL import Image
import cv2
from deploy import settings
import os
>>>>>>> 11078f194c8998bf80a3043f27b686b91ac7046b
# from django.core.files.storage import FileSystemStorage

# Create your views here.

INPUT_SIZE = (256, 256)

def success(request):
<<<<<<< HEAD
    
    loaded_model = tf.keras.models.load_model("template/prekshyaandsrishti.h5")
    loaded_model.build()
    return render(request, 'success.html')
=======
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
>>>>>>> 11078f194c8998bf80a3043f27b686b91ac7046b


def image_upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ImageForm()
<<<<<<< HEAD
    return render(request, 'image_upload.html', {'form': form})


# # Intermediate resizing as a bottleneck.
#     bottleneck = layers.Resizing(
#         *TARGET_SIZE, interpolation=interpolation
#     )(x)

#     # Residual passes.
#     for _ in range(num_res_blocks):
#         x = res_block(bottleneck)

#     # Projection.
#     x = layers.Conv2D(
#         filters=filters, kernel_size=3, strides=1, padding="same", use_bias=False
#     )(x)
#     x = layers.BatchNormalization()(x)

#     # Skip connection.
#     x = layers.Add()([bottleneck, x])

#     # Final resized image.
#     x = layers.Conv2D(filters=3, kernel_size=7, strides=1, padding="same")(x)
#     final_resize = layers.Add()([naive_resize, x])

#     return tf.keras.Model(inputs, final_resize, name="learnable_resizer")
=======
    return render(request, 'image_upload.html', {'form': form})
>>>>>>> 11078f194c8998bf80a3043f27b686b91ac7046b
