from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import os
from django.http import JsonResponse
from .models import *
from datetime import datetime
# Create your views here.
def login(request):
    return render(request,'loginpage.html')
def signup(request):
    return render(request,'signpage.html')
def create(request):
    if request.method=="POST":
        fname=request.POST['first']
        lname=request.POST['last']
        mailid=request.POST['mail']
        uname=request.POST['user']
        pwd=request.POST['pass']
        user=User.objects.create_user(
            first_name=fname,
            last_name=lname,
            username=uname,
            password=pwd,
            email=mailid,
            
        )
        user.save()
        auth.login(request,user) 
        return redirect('homepage')

        
    else:
        return redirect('signup')
def loginhere(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            if user.is_active:
                auth.login(request,user) 
                return redirect('homepage')
            else:
                return redirect('login')
                
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('login')
    else:
        return redirect('login')
    
def homepage(request):
    cat=RoomCategory.objects.all()
    rm=Room.objects.all()
    return render(request,'home.html',{'cat':cat,'rm':rm})
def addcat(request):
    if request.method=='POST':
        name=request.POST['name']
        bprice=request.POST['price']
        cat=RoomCategory(name=name,base_price=bprice)
        cat.save()
        return redirect('homepage')

def addroom(request):
    if request.method=='POST':
        rno=request.POST['rnmbr']
        sel=request.POST['category']
        cat1=RoomCategory.objects.get(id=sel)
        avail='True'
        rooms=Room(room_number=rno,category=cat1,is_available=avail)
        rooms.save()
        return redirect('homepage')
def roomlist(request):
    room=RoomCategory.objects.all()
    list=Room.objects.all()
    return render(request,'roomlistview.html',{'list':list,'room':room})
def addreserv(request):
    room=RoomCategory.objects.all()
    list=Room.objects.all()
    return render(request,'reservation.html',{'list':list,'room':room})
def editroom(request,id):
    
    editcat=Room.objects.get(id=id)
    return render(request,'roomlistview.html',{'editcat':editcat,})
def roomediting(request,id):
    if request.method=='POST':
        cats=request.POST.get('category')
        cat=RoomCategory.objects.get(id=cats)
        room=Room.objects.get(id=id)
        room.category=cat
        room.room_number=request.POST['rnmbr']
        room.save()
        return redirect('roomlist')
def logout(request):
    return render(request,'loginpage.html')
