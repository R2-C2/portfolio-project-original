from django.db import models
from django.conf import settings

class Resume(models.Model):
    title = models.TextField(max_length=200)
    document = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.title
