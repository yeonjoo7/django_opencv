from django.shortcuts import render
from .forms import SimpleUploadForm,ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face

# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def simple_upload(request):# 이거 대신 아래의 detect_face(DB사용)을 씀

    if request.method =='POST':
        # print(request.POST)
        # print(request.FILES)
        # print(request.FILES['image'])
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # DB를 안쓸때 쓰는 방법
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            context = {'form':form, 'uploaded_file_url':uploaded_file_url}
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else:
        form = SimpleUploadForm()

        context = {'form':form}
        return render(request, 'opencv_webapp/simple_upload.html', context)

def detect_face(request):
    if request.method=='POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            # 얼굴과 눈을 찾는 opencv를 넣는 장소
            post.save()
            # post.upload_at  #확인용
            #
            imageURL = settings.MEDIA_URL + form.instance.document.name
            # print()
            # print('*****')
            # print(form.instance, form.instance.document.name, form.instance.document.url)
            # print()
            cv_detect_face(settings.MEDIA_ROOT_URL+imageURL)

            context = {'form':form, 'post':post}
            return render(request, 'opencv_webapp/detect_face.html', context)

    else:
        form = ImageUploadForm()
        return render(request, 'opencv_webapp/detect_face.html', {'form':form})
