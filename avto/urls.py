from django.urls import path
from . import views
urlpatterns = [

    path('', views.AvtoView.as_view(), name='view'),
    path('add/', views.Add_avto.as_view(), name='add'),
    path('view/', views.AvtoView.as_view(), name='view'),

]