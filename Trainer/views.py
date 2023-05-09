from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from accounts.models import CustomUser
from .models import Gymgoer,Trainers

def about(request):
    if request.user.is_authenticated:
        print("accountcheck")
        return redirect("check")
    return render(request, "homepage/home.html")


def account_check(request):
    myquery=CustomUser.objects.all().filter(username=request.user)
    if myquery[0].accountconfigured:
        print("user was configured")
        return redirect("dashboard")
    else:
        print("user was not configured")
        return redirect("configure")

def configure(request):
    if request.method=="POST":
        print(request.POST["usertype"])
        print(request.POST['goal'])
        print(request.user)
        insert_configuration_data(usertype=request.POST["usertype"],user=request.user,goal=request.POST['goal'])
        return redirect("dashboard")
    return render(request,"configure/configure.html")


#def gymconnections(request):
    #return render(request,"gymconnections/gymconnections.html")



def insert_configuration_data(usertype,user,goal):
    if usertype=="normaluser":
        newnormal=Gymgoer(name=user,goaldescription=goal)
        newnormal.save()
        CustomUser.objects.filter(username=user).update(accountconfigured=True)
        print("normaluserhere")
    elif usertype=="trainer":
        print(user.pk)
        newtrainer=Trainers(name=user,methodsdescription=goal)
        newtrainer.save()
        CustomUser.objects.filter(username=user).update(accountconfigured=True)
        print("trainerhere")
    else:
        return redirect("configure")