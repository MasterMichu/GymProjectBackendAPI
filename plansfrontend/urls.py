from django.urls import  path
from . import views
urlpatterns = [
    path("",views.preview, name="preview2"),
    #path("addplan/",views.addplan, name="addplan"),
    #path("recordresults/<plan>",views.record, name="record"),
]