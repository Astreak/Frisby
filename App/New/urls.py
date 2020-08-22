from django.urls import path,include
from . import views
from django.contrib.auth.models import User
from .models import car
import json

urlpatterns = [
    path("",views.home1,name="main-home2"),
    path("<int:name>",views.home2,name="main-home1"),
    path("about/",views.about,name="main-about"),
    path("users/",views.users,name="main-users"),
    path("info/<int:id>/",views.get_fucking_info,name="main-info"),
    path("forms/",views.forms1,name="main-forms1"),
    path("msg/",views.forms2,name="main-msg"),
    path("create/",views.usercreate,name="main-create"),
    path("profile/",views.profile,name="main-profile"),
    path("music/",views.musicform,name="main-music"),
    path("medical/",views.medical,name="main-medical"),
    path("kol/",views.current,name="main-current")
    
    
        
]
K=User.objects.all()
with open("A.json","w") as file:
    for j in K:
         for i in j.car_set.all():
            json.dump({"name":i.name,"price":i.price,"color":i.color},file)

