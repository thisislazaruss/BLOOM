from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
def hotel_image_view(request):

	if request.method == 'POST':
		form = breastcancerForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = breastcancerForm()
	return render(request, 'breastcancer_image_form.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')

# def predictImage(request):
#     from keras.preprocessing.image import img_to_array, load_img
#     from django.core.cache import cache
#     from django.urls import reverse
#     image_width = 256
#     image_height = 256

#     f = request.FILES['filePath']
#     filepath='./media/'
#     files=filepath+f.name\

#     fs = FileSystemStorage(location=filepath)
#     filePathName = fs.save(f.name, f)
#     testimage = './media/'+person.user.username+'/'+filePathName

#     original = load_img(testimage, target_size=(image_width, image_height))
#     numpy_image = img_to_array(original)

#     label, remarks, confidence = predict(model, numpy_image)
#     records = Record.objects.create(lungs_status=label, remarks=remarks,
#                     x_ray=testimage, person=person,confidence=confidence)
#     else:
#         import datetime
#         record=Record.objects.get(x_ray=files)
#         offset=datetime.timezone(datetime.timedelta(hours=5,minutes=45))
#         record.test_date=datetime.datetime.now(offset)
#         record.save()

#     person_data=fetchrecentreports(request.user)
#     filePathName=person_data[0][1].x_ray
#     label=person_data[0][1].lungs_status
#     remarks=person_data[0][1].remarks
#     confidence=person_data[0][1].confidence
#     context = {'filePathName': filePathName,
#                'label': label, 'remarks': remarks, 'confidence': confidence}
#     context['person_data']=person_data
#     cache.delete(reverse('predictImage'))
#     return render(request, "main/index.html", context)