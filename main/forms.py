from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from .models import Post
class RegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','first_name','last_name','password1','password2']



class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
