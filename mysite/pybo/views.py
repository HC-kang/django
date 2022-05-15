from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 Sherry 욕하지 마세요. 마음 착하게 쓰세요.")
