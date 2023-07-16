from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(req):
    posts = models.post.objects.all()
    return render(req, 'templates/board/index.html', {
        'post_list' : posts
    })
