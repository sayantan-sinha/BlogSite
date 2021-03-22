from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import os

# Create your models here.

class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Post(models.Model):
    image_storage = FileSystemStorage(
        # Physical file location ROOT
        location=os.path.join(settings.MEDIA_ROOT, 'blogapp'),
        # Url for file
        base_url=os.path.join(settings.MEDIA_URL, 'blogapp')
    )

    def image_directory_path(self, filename):
        return os.path.join('pics', filename)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to=image_directory_path, storage=image_storage)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title