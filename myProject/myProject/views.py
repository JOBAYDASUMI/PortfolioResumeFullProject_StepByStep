from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def homePage(req):
    
    return render(req,'common/homePage.html')


def logoutPage(req):
    logout(req)
    return redirect("loginPage")

def loginPage(req):
    if req.method == 'POST':
        Username=req.POST.get('username')
        Password=req.POST.get('password')
        user = authenticate(username=Username,password=Password)
        
        if user:
            login(req,user)
            return redirect("jobFeedPage")
        else:
            messages.worning(req,"User Not Found")
    
    return render(req,'common/loginPage.html')

def registerPage(req):
    if req.method == 'POST':
        Username=req.POST.get('username')
        Usertype=req.POST.get('usertype')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        Confirmpassword=req.POST.get('confirmpassword')
        
        if Password == Confirmpassword:
            user = Custom_User.objects.create_user(
                username=Username,
                user_type=Usertype,
                email=Email,
                password=Confirmpassword,
                
            )
        messages.success(req,"Account Create Success fully")
        return redirect("loginPage")
        
    
    return render(req,'common/registerPage.html')


def jobFeedPage(req):
    
    return render(req,'includes/jobFeedPage.html')
