from django.shortcuts import render,redirect
from blog.models import Post,Comment
from .forms import CommentForm,PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView


# Create your views here.
def blog_index(request):
	posts=Post.objects.all().order_by('-created_on')
	context={
		"posts":posts,
	}
	return render(request,"blog_index.html",context)


def blog_detail(request,title):
	post=Post.objects.get(title__contains=title)
	form=CommentForm()

	
	if request.method =='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=Comment(
				author=form.cleaned_data["author"],
				body=form.cleaned_data["body"],
				post=post
				)
			comment.save()
	
	comments=Comment.objects.filter(post=post)
	context={
			"post":post,
			"comments":comments,
			"form":form,
		}
	return render(request,"blog_detail.html",context)

		
def add_post(request):
	form=PostForm(user=request.user)
	
	return render(request,'add_post.html',{'form':form})
		

			