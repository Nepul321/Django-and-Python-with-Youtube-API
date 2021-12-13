from .views import (
    HomeView
)

from django.urls import path

urlpatterns = [
    path('', HomeView, name="home"),
    path('search/', HomeView, name="search")
]
