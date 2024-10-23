from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('create',views.create,name='create'),
    path('loginhere',views.loginhere,name='loginhere'),
    path('homepage',views.homepage,name='homepage'),
    path('addcat',views.addcat,name='addcat'),
    path('addroom',views.addroom,name='addroom'),
    path('roomlist',views.roomlist,name='roomlist'),
    path('addreserv',views.addreserv,name='addreserv'),
    path('editroom/<int:id>',views.editroom,name='editroom'),
    path('roomediting/<int:id>',views.roomediting,name='roomediting'),
    path('logout',views.logout,name='logout'),
]
