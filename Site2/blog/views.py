from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.views import View

def view_login(request):
     if request.method == 'POST':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username, password=password)
               if user is not None:
                    login(request, user)
                    return redirect('home')
     else:
          form = AuthenticationForm()
     return render(request, 'login.html', {'form': form})


# Create your views here.
def index(request):
     posts = Post.objects.all()
     return render(request, 'index.html', {"posts": posts})

def detail(request, pk):
     post = Post.objects.get(id=pk)
     return render(request, 'detail.html', {"post": post})

def logout_view(request):
     logout(request)
     return redirect(logout)

class Register(View):
     form_class = UserCreationForm
     template_name = 'register.html'

     def get(self, request):
          form = self.form_class()
          return render(request, self.template_name, {'form': form})

     def post(self, request):
          form = self.form_class(request.POST)
          if form.is_valid():
               user = form.save()
               return redirect('login')
          return render(request, self.template_name, {'form': form})
