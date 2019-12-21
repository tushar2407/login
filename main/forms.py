from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.db import models
#from uploads.core.models import Document
from .models import UserProfile

class RegisterationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model= User
        fields =('username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2'
        )
    def save(self,commit=True):
        user=super(RegisterationForm,self).save(commit=True)
        user.first_name=self.cleaned_data('first_name')
        user.last_name=self.cleaned_data('last_name')
        user.email=self.cleaned_data('email')
        #user.password=cleaned_data('password')
        if commit:
            user.save()
class EditProfile(UserChangeForm):
    class Meta:
        model=User
        fields=('first_name','email','password')
        exclude=()
class UploadFile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('file','file_name')