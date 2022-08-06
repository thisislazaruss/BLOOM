from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import success, image_upload

urlpatterns = [
    path('', image_upload, name="image-upload"),
    path('success/', success, name="success"),
    #path('image_upload/', image_upload, name="image-upload"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


