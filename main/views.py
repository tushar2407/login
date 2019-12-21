from django.shortcuts import render, redirect
from django.contrib.auth.forms import(
     UserCreationForm, 
     PasswordChangeForm
)
from main.forms import RegisterationForm, EditProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm 
from django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.models import User
#from django.contrib.auth import LoginView
# Create your views here
def home(request):
    numbers=[1,2,3,4]
    name='Tushar Mohan'
    args={'myName':name,'numbers':numbers,'user':request.user}
    return render(request,'accounts/home.html',args)
def register(request):
    if request.method=='POST':
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=RegisterationForm()
        args={'form':form}
        return render(request,'accounts/register.html',args)
    return render(request,'accounts/login.html')
@login_required
def profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

def edit_profile(request):
    if request.method=='POST':
        form=EditProfile(request.POST,instance=request.user)
        #form=request.user
        if form.is_valid:
            form.save()
            return redirect('/accounts/profile')
    else:
        form=EditProfile(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        #form=request.user
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)
    #return render(request,'accounts/home.html')

"""
----update_session_auth_hash(request, user='')
is needed to redirect to the user changing the password, otherwise  it may redirect to some anonymous user


"""