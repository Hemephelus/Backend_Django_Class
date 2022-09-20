from email import message
from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

1
def home(request):
    posts = Post.objects.all()
    return render(request,'my_blog_app/home.html', {'posts':posts})


def past_page(request):
    post = Post.objects.first()
    return render(request,'my_blog_app/PostPage.html', {'post':post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'Hello {username}, Your account has been created successfully')
            return redirect('homepage')

    else:
        form = UserCreationForm()

    return render(request,'my_blog_app/signup.html', {'form':form})
