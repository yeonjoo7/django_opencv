from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'opencv_webapp'

# 최대한 경로명, 함수명, 네임 다 일치시켜주는게 편함
urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
