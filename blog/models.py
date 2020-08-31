from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=20)
	def __str__(self):
		return self.name

class Post(models.Model):
	title=models.CharField(max_length=225)
	body=RichTextUploadingField(blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	last_modified=models.DateTimeField(auto_now=True)
	categories=models.ManyToManyField('Category',related_name='posts')
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title


class Comment(models.Model):
	author=models.CharField(max_length=60)
	body=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	post=models.ForeignKey('Post',on_delete=models.CASCADE)
	def __str__(self):
		return self.author

