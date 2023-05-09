from django.shortcuts import render
import requests
endpoint="http://127.0.0.1:8000/"
# Create your views here.
def preview(request):
    get_response=requests.get(endpoint+"plansapi/",params="kaszanka")
    print(get_response)
    print(get_response.json())

    return render(request, "plans/preview.html", get_response)