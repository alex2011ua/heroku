from django.urls import path
from . import views
urlpatterns = [

    path('index', views.Start.as_view(), name='index'),
    path('add', views.Add_avto.as_view(), name='add'),
    path('view', views.AvtoView.as_view(), name='view'),

]