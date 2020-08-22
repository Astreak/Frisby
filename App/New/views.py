from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import *

def home2(req,name):
    return HttpResponse(f"<h1> <center>There is a massive way of going there is it ok mr.{name} </center> </h1>")
def home1(req):
    return HttpResponse("<h1> <center>There is a massive way of going there is it ok </center> </h1>")
    
def about(req):
    return HttpResponse("<h1> This is a great fortune of going there </h1>")

def users(req):
    O=User.objects.all()
    L=[i.username+" " for i in O]
    return HttpResponse(L)
def  get_fucking_info(req,id):
    O=User.objects.get(pk=id)
    K=O.car_set.all()
    L=[]
    for k in K:
        L.append(f"<h1><center> cars by mr. {O.username}<br> is {k.name}</h1>\n")
    return HttpResponse(L)
@csrf_protect
def forms1(req):
    if req.method=="POST":
        form=CarForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-home2")
    else:
        form=CarForm()
    return render(req,"New/car_form.html",{"form":form})

def forms2(req):
    if req.method=="POST":
        form=MsgForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-home2")
    else:
        form=MsgForm()
        
    return render(req,"New/msg_form.html",{"form":form})
def usercreate(req):
    if req.method=="POST":
        form=CreateUser(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-home2")
    else:
        form=CreateUser()
    return render(req,"New/create_user.html",{"form":form})

def profile(req):
    K=f"<h1> hello mr.{req.user}"
    O=req.user.msg_set.all()
    L=[]
    for i in O:
        L.append(f"<center><h1> {i.sen} <br> {i.text}</h1></center>")
    return HttpResponse(L)

def musicform(req):
    if req.method=="POST":
        form=MusicForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-home2")
    else:
        form=MusicForm()
    return render(req,"New/music_form.html",{"form":form})
def current(req):
    if req.user:
        return HttpResponse(f"<h1><center>{req.user}</center></h1>")
    else:
        return HttpResponse("You havent logged in yet");
    
def medical(req):
    if req.method=="POST":
        form=MedicalForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("main-home2")
    else:
        form=MedicalForm()
    return render(req,"New/medical_form.html",{"form":form})