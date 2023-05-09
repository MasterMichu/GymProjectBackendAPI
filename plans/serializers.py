from rest_framework import serializers
from .models import Plans, Traninglog,AvilableExcercises, Musclesgroup,PlanName, PlanName
from django.conf import settings
from accounts.models import CustomUser

class PlanSerializer(serializers.ModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    #planname = serializers.SlugRelatedField(queryset=PlanName.objects.all(), slug_field="name")
    planname = serializers.PrimaryKeyRelatedField(queryset=PlanName.objects.all())
    excercise = serializers.SlugRelatedField(queryset=AvilableExcercises.objects.all(), slug_field="name")
    my_field = serializers.SerializerMethodField('excerciseId')

    def excerciseId(self,avilableExcercises):
        return int(avilableExcercises.excercise.id)
    class Meta:
        model = Plans
        fields = ["id","excercise","planname","my_field"]

class PlanUniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanName
        fields = ['name',"id"]


class PlanExcerciseSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    excercise = serializers.SlugRelatedField(queryset=AvilableExcercises.objects.all(), slug_field="name")
    #planname=serializers.SlugRelatedField(queryset=PlanName.objects.all(),slug_field="name")
    planname = serializers.PrimaryKeyRelatedField(queryset=PlanName.objects.all())
    class Meta:
        model=Plans
        fields=["id","planname","excercise","owner"]


class TraningLogSerializer(serializers.ModelSerializer):
    excercise = serializers.SlugRelatedField(queryset=AvilableExcercises.objects.all(), slug_field="name")
    class Meta:
        model = Traninglog
        fields=["id","excercise","reps","weight","date"]

class AvilableExcercisesSerializer(serializers.ModelSerializer):
    musclesgroup= serializers.SlugRelatedField(queryset=Musclesgroup.objects.all(),slug_field="name")

    class Meta:
        model=AvilableExcercises
        fields=["id","name","musclesgroup"]

class ExcercisesDetails(serializers.ModelSerializer):
    musclesgroup= serializers.SlugRelatedField(queryset=Musclesgroup.objects.all(),slug_field="name")
    my_field = serializers.SerializerMethodField('MusclesGroupImage')

    def MusclesGroupImage(self,avilableExcercises):
        return "http://127.0.0.1:8000/"+str(Musclesgroup.objects.get(id=avilableExcercises.musclesgroup.id).image)
    class Meta:
        model=AvilableExcercises
        fields=["id","name","musclesgroup","image","my_field","description"]