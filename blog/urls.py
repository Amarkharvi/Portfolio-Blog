from django.urls import path,re_path
from . import views

 
urlpatterns=[
	path("",views.blog_index,name="blog_index"),
	path("<pname>/" ,views.blog_detail,name="blog_detail"),
	#path('<int:pk>/', 
       # PostDetailView.as_view(), 
       # name='detail'),
	path("<category>/",views.blog_category,name="blog_category")
	]