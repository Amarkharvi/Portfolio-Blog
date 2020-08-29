from django.urls import path,re_path
from . import views

 
urlpatterns=[
	path("",views.blog_index,name="blog_index"),
	path("addPost/" ,views.add_post,name="add_post"),
	path("<title>/" ,views.blog_detail,name="blog_detail"),
	]