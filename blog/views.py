from django.shortcuts import render,redirect
from blog.models import Post,Comment,Category
from .forms import CommentForm,PostForm,UpdatePost,DeletePost
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
def blog_index(request):
	posts=Post.objects.all().order_by('-created_on')
	context={
		"posts":posts,
	}
	return render(request,"blog_index.html",context)


def blog_detail(request,title,pk):
	post=Post.objects.get(pk=pk)
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

@login_required		
def add_post(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			id=form.cleaned_data.get("categories")
			p_id=form.cleaned_data.get("title")
			body=form.cleaned_data.get("body")
			Posts=form.save(commit=False)
			
			categories=Category.objects.filter(name=id)
			instance=Post.objects.create(author=request.user,title=p_id,body=body)
			for category in categories:
				instance.categories.add(category)
			
			Posts.author=request.user
			return redirect('blog_index')
	form=PostForm()		

	
	return render(request,'add_post.html',{'form':form})

@login_required
def update_post(request,title,pk):
	obj=get_object_or_404(Post,pk=pk)
	if request.method=='POST':
		u_form=UpdatePost(request.POST,instance=obj)
		if u_form.is_valid():
			id=u_form.cleaned_data.get("categories")
			p_id=u_form.cleaned_data.get("title")
			body=u_form.cleaned_data.get("body")
			Posts=u_form.save(commit=False)
			
			categories=Category.objects.filter(name=id)
			
			for category in categories:
				obj.categories.add(category)
				
			Posts.author=request.user
			Posts.save()
			return redirect('blog_index')
			
	u_form=UpdatePost(instance=obj)
	context={
		'u_form':u_form,
	}		

	return render(request,'update_post.html',context)

@login_required
def delete_post(request,pk):
	post=get_object_or_404(Post,pk=pk)
	if request.method == "POST":
		form=DeletePost(request.POST,instance=post)
		if form.is_valid():
			post.delete()
			return redirect('blog_index')
	form=DeletePost(instance=post)
	return render(
		request,
		'delete_post.html',
		{
			'form':form,
			'post':post,
		}
	)
  
			