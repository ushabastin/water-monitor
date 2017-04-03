from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest,HttpResponse
from django.utils import timezone
from .forms import NodenameForm
from .models import Nodename


# Create your views here.

def post_list(request):
    posts = Nodename.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'repository/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Nodename, pk=pk)
    return render(request, 'repository/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = NodenameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NodenameForm()
    return render(request, 'repository/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Nodename, pk=pk)
    if request.method == "POST":
        form = NodenameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NodenameForm(instance=post)
    return render(request, 'repository/post_edit.html', {'form': form})


#3rd Class  https://docs.djangoproject.com/en/1.7/intro/tutorial03/

def detail(request, id):
    return HttpResponse("You're looking at Node %s." % id)

def results(request, id):
    response = "You're looking at the Sensor data of Node %s."
    return HttpResponse(response % id)

