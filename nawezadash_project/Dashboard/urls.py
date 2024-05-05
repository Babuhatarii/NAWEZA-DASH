from django.urls import path
from .views import activity_detail

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:activity_id>/", views.activity_detail, name='activity_detail'),
]
