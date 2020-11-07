from django.urls import path

from . import views

app_name = "FRApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("scan/", views.scan, name="scan"),
]
