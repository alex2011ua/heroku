from django.urls import path, re_path
from . import views
urlpatterns = [

    path('', views.AvtoView.as_view(), name='view'),
    path('add/', views.Add_avto.as_view(), name='add'),
    path('view/', views.AvtoView.as_view(), name='view'),
    path('dell/', views.AvtoDell.as_view(), name='dell'),
    re_path('view/dell/(?P<nomber>\w+)/$', views.AvtoDellConfirm.as_view(), name='dell'),



]