from django.urls import path
from . import views


urlpatterns = [
    path('', views.Weather.as_view(), name='weather'),
    ]