# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# from django.core.files.storage import FileSystemStorage

# Create your views here.
def success(request):
	return HttpResponse('successfully uploaded')


def image_upload(request):

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')

    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})



