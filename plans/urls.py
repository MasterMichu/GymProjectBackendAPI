from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("plans/",views.UsersPlansList.as_view(), name="preview"),
    path("addplan/",views.PlansLookupAndCreatePlans.as_view(), name="PlansLookupAndCreatePlans"),
    path("excercises/",views.AllExcercisesLookup.as_view(), name="AllExcercisesLookup"),
    path("recordresults/",views.RecordTraningResults, name="record"),
    path("delete/<int:pk>",views.DelatePlanAPI.as_view(), name="DelatePlanAPI"),
    path("deleteplanname/<int:pk>",views.UsersPlansListDelate.as_view(), name="DelatePlanNameAPI"),
    #re_path("^previewexercisesonplan/(?P<planname>.+)/$",views.PreviewExercisesOnPlan.as_view(), name="PreviewExercisesOnPlan"),
    path("previewexercisesonplan/<int:pk>",views.PreviewExercisesOnPlan.as_view(), name="PreviewExercisesOnPlan"),
    path("trainingresults/",views.RetriveTrainingResults, name="RetriveTrainingResults"),
    path("excercisedetails/<int:pk>",views.ExcerciseDetails.as_view(), name="ExcerciseDetails"),
]