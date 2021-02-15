from django.urls import path
from . import views
urlpatterns = [
    path('', views.Start.as_view(), name='index'),
    path('index/export/', views.Export.as_view(), name='export'),
]
