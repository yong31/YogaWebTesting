from django.urls import path

from . import views

urlpatterns = [
    path('teststress', views.teststress, name='teststress'),
]
