from django.shortcuts import render
from .forms import RegisterForm,CreatePost
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Post 

from django.core.mail import send_mail,send_mass_mail

@login_required(login_url='/login')
def home(request):
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
            return HttpResponseRedirect(reverse('home'))
    posts = Post.objects.all()
    return render(request,'main/home.html',{
        'posts': posts
    })




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
            
    return render(request,'main/register.html',{
        'form': RegisterForm()
    })


@login_required(login_url='/login')
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return HttpResponseRedirect(reverse('home'))
            
    return render(request,'main/create_post.html',{
        'form': CreatePost()
    })



