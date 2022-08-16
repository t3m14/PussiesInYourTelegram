from django.http import HttpResponse
from django.shortcuts import render
from . import tasks
# Create your views here.
def home(request):
    tasks.download_a_cat_img.delay()
    return HttpResponse("<h1>Гружу кота!</h1>")