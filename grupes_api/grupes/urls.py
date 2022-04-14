from django.contrib import admin
from django.urls import path, include
from .views import BandList

urlpatterns = [
    path('bands', BandList.as_view()),
]