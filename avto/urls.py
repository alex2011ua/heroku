from django.urls import path
from . import views
urlpatterns = [

    path('', views.Start.as_view(), name='index'),
    path('add', views.Add_avto.as_view(),

         )
]