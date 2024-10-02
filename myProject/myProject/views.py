from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse


def homePage(req):
    
    return render(req,'common/homePage.html')