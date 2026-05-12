from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse("Home")


def sobre(request):
    return HttpResponse("Sobre")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("sobre/", sobre),
]
