from django.shortcuts import render,redirect
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {"blogdata" : blogs})

def postcreate(request):
    if(request.POST['title'] == '' or request.POST['body'] == '' or request.method != 'POST'):
        return render(request, 'none.html')
    if(request.POST.get('not_human', False)):
        return render(request, 'not_human.html')
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')

def postnew(request):
    return render(request, 'create.html')
