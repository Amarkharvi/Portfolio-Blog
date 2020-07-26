from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
	title=models.CharField(max_length=100)
	description=RichTextUploadingField(blank=True)
	technology=models.CharField(max_length=20)
	image=models.ImageField(upload_to='img/')
	def __str__(self):
		return self.title