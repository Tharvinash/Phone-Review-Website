from . import views
from django.urls import path

# Flow URL --> View 
urlpatterns = [
    path("", views.main, name='model-list'),
    path("<str:model>", views.specificModel, name='specific-model'),
    path("<str:model>/<slug:slug>", views.reviews, name='reviews')
]
