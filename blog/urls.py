from django.urls import path,re_path
from . import views

 
urlpatterns=[
	path("",views.blog_index,name="blog_index"),
	path("addPost/" ,views.add_post,name="add_post"),
	path("<title>/<int:pk>/" ,views.blog_detail,name="blog_detail"),
	path("<int:pk>/deletePost/" ,views.delete_post,name="delete_post"),
	path("<title>/<int:pk>/updatePost/" ,views.update_post,name="update_post"),

	]