from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    # form의 빈칸 허용: blank=True
    description = models.CharField(max_length=255, blank=True)
    # 자동으로 폴더 이름을 연/월/일로 찾아가서 저장됨
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    upload_at = models.DateTimeField(auto_now_add=True)
