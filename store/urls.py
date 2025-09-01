from django.urls import path
from .views import Home

app_name = "store"

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
