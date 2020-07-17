from django.urls import path
from . import views
urlpatterns = [

    path('', views.AvtoView.as_view()),
]