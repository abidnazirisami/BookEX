from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('This project will be turned into BookEX. Stay tuned!')