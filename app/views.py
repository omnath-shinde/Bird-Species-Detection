from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage
from .utils import empty_media, processed_img
from .models import UserData
import os


# Create your views here.
def home(request):
    # delete all files in folder
    # empty_media('media/')

    if request.method == 'POST':
        myfile = request.FILES['myfile']

        u = UserData()
        u.name = request.POST.get('name')
        u.image = myfile
        u.save()

        uploaded_file_url = str(u.image)
        result = processed_img(uploaded_file_url)

        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url,
            'result': result,
        })
    return render(request, 'index.html', {})
