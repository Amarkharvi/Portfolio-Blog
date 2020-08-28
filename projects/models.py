from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import Post,Category
# Create your models here.
class Project(models.Model):
	title=models.ForeignKey(Post,on_delete=models.CASCADE)
	description=RichTextUploadingField(blank=True)
	category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
	image=models.ImageField(upload_to='img/')
	def __str__(self):
		return f'{self.title}'