from django.shortcuts import render,redirect
from .forms import RegistrationForm,UpdateUser,UpdateProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'your account has been created for {username}!!, now u can sign in, thank you!')
            return redirect('login')

    else:
        form=RegistrationForm()      

    return render(request,'users/register.html',{'form':form})      


def Login(request):
    if request.user.is_authenticated:
        return redirect('project_index')

    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(
            request,
            username=username,
            password=password
        )  

        if user is not None:
            form=login(request,user)
            messages.success(request,f'Welcome {username}')
            return redirect('project_index')


    form = AuthenticationForm()
    return render(request,'users/login.html',{'form':form})       
  

def Logout(request):
      logout(request)
      return render(request,'users/logout.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UpdateUser(request.POST,instance=request.user)
        p_form=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request,f'Your Profile has been Updated!!')
            return redirect('profile')

    else :
        u_form=UpdateUser(instance=request.user)
        p_form=UpdateProfile(instance=request.user.profile)



    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/profile.html',context)        

      