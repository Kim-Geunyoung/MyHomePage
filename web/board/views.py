from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(req):
    return render(req, 'board/index.html')

def main(req):
    return render(req, 'board/main.html')
