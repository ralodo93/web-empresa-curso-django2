from django.urls import path
from . import views as core_views

urlpatterns = [
    path("", core_views.home, name="home"),
    path("store/", core_views.store, name="store"),
    path("about/", core_views.about, name="about"),
]