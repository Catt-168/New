from django.urls import path
from .views import home

app_name = "port"
urlpatterns = [
    path('', home, name="home-view"),
]