# Create your views here.
from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
import tensorflow as tf
import h5py

# from django.core.files.storage import FileSystemStorage

# Create your views here.


def success(request):
    
    loaded_model = tf.keras.models.load_model("template/prekshyaandsrishti.h5")
    loaded_model.build()
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