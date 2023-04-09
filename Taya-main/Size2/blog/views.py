from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django .contrib.auth import authenticate, login, logout

def view_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html', {"posts": posts}) 

def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request,'detall.html', {"post": post}) 

