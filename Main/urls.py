from . import views
from django.urls import path

# Flow URL --> View 
urlpatterns = [
    path("", views.main, name='index'),
]