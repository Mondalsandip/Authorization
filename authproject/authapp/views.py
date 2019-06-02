from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import SignupForm,UserEditForm
# Create your views here.
def home(request):
    return render(request,'authapp/home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in ')
            return redirect ('home')
        messages.success(request,'Error')
        return redirect ('login')
    return render(request,'authapp/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'successfully logout')
    return redirect ('home')

def register_user(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'successfully register')
            return redirect('home')
    form=SignupForm()
    context={
    'form':form
    }
    return render (request,'authapp/register.html',context)

def profile_edit(request):
    if request.method == 'POST':
        form=UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully updated')
            return redirect('home')
    form=UserEditForm(instance=request.user)
    context={
    'form':form
    }
    return render(request,'authapp/edit.html',context)
