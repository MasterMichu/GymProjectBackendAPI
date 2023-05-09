from django.http import HttpResponse
from rest_framework.response import Response


def about(request):
    return HttpResponse("Below You can find list of endpoints of designed api: \n site is being modified at the moment- sorry")