from django.shortcuts import render, redirect
from .models import Plans,AvilableExcercises, Musclesgroup ,Traninglog,PlanName
from datetime import date
from rest_framework import generics
from django.conf import settings
from django.utils.text import lazy
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import PlanUniqueSerializer,PlanSerializer, PlanExcerciseSerializer,TraningLogSerializer, AvilableExcercisesSerializer,ExcercisesDetails
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


class PreviewExercisesOnPlan(generics.ListAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsOwner, IsAuthenticated]
    lookup_field = ["pk"]
    def get_queryset(self, *args, **kwargs):
        print (self.args)
        print(self.kwargs)
        userplans=Plans.objects.all().filter(owner=self.request.user.id)
        qs=userplans.filter(planname=self.kwargs["pk"])
        return qs

class UsersPlansList(generics.ListCreateAPIView):
    queryset=PlanName.objects.all()
    serializer_class = PlanUniqueSerializer
    #permission_classes = [IsOwner,IsAuthenticated] #dangerous

    def get_queryset(self, *args, **kwargs):
        userplans=PlanName.objects.all() .filter(owner=self.request.user.id) # dangerous
        return userplans
    def perform_create(self, serializer):
        if PlanName.objects.all().filter(owner=self.request.user, name=self.request.data["name"]).exists():
            raise ValidationError(
            message='MyModel with this (name and owner) already exists.',
            code='unique_together')
        serializer.save(owner=self.request.user)


class UsersPlansListDelate(generics.DestroyAPIView):
    queryset=PlanName.objects.all()
    serializer_class = PlanUniqueSerializer
    lookup_field = "pk"

class PlansLookupAndCreatePlans(generics.CreateAPIView):
    queryset=Plans.objects.all()
    serializer_class = PlanExcerciseSerializer
    permissions_classes = [IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        userplans=Plans.objects.all().filter(owner=self.request.user)
        return userplans
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class AllExcercisesLookup(generics.ListAPIView):
    queryset = AvilableExcercises
    serializer_class = AvilableExcercisesSerializer
    def get_queryset(self):
        return AvilableExcercises.objects.all()
    
class ExcerciseDetails(generics.RetrieveAPIView):
    queryset = AvilableExcercises
    serializer_class = ExcercisesDetails
    lookup_field = "pk"
    def get_queryset(self):
        return AvilableExcercises.objects.all()

@api_view(["POST","GET"])
def RecordTraningResults(request):
    if request.method=="POST":
        print("post")
        instance=Traninglog(owner=request.user,
                            excercise=AvilableExcercises.objects.get(name=request.data["excercise"]),
                            reps=request.data["reps"],
                            weight=request.data["weight"],
                            date=request.data["date"])
        serializer=TraningLogSerializer(instance,data=request.data)
        if not serializer.is_valid():
            error = {"error": "validation error"}
            return Response(error)
        serializer.save()
    queryset=Traninglog.objects.filter(owner=request.user)
    serializer=TraningLogSerializer(queryset,many=True)
    return Response(serializer.data)


class DelatePlanAPI(generics.DestroyAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlanExcerciseSerializer
    permissions_classes = [IsAuthenticated,IsOwner]
    lookup_field = "pk"
    def get_queryset(self, *args, **kwargs):
        userplans = Plans.objects.all().filter(owner=self.request.user)
        return userplans

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, serializer):
        serializer_instance=Plans.objects.get(id=self.kwargs["pk"])
        serializer_instance.delete()
@api_view(["GET"])
def RetriveTrainingResults(request):
    if request.method == "GET":
        allTrainingResults= Traninglog.objects.all().filter(owner= request.user)
        ExcercisesUnique= allTrainingResults.values_list("excercise").distinct()
        print(ExcercisesUnique)
        responselist=[]
        tempresponsedict={}
        #print(dir(allTrainingResults.order_by("date")))
        for i in ExcercisesUnique:
            print(i[0])
            tempresponsedict["name"]=AvilableExcercises.objects.get(id=i[0]).name
            tempresponselist=[["date","weight","reps"]]
            for j in allTrainingResults.filter(excercise=i[0]).order_by("date"):
                print(j.date)
                tempresponselist.append([j.date.strftime("%m/%d/%Y"),j.weight,j.reps])
            tempresponsedict["results"]=tempresponselist
            responselist.append(tempresponsedict)
            tempresponsedict={}
        print(responselist)
        return Response(responselist)











