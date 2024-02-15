from django.urls import path

from . import views

urlpatterns = [
    path("myapp01/", views.members, name="myapp01"),
]
