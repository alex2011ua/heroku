from django.urls import path, re_path
from . import views, baza
urlpatterns = [

    path('', views.AvtoView.as_view(), name='view'),
    path('add/', views.AddAvto.as_view(), name='add'),
    path('view/', views.AvtoView.as_view(), name='view'),
    re_path(r'view/dell/(?P<nomber>\w+)/$', views.AvtoDell.as_view(), name='dell'),
    re_path(r'view/dell/(?P<nomber>\w+)/dell$', views.AvtoDellConfirm.as_view(),
            name='dell_confirm'),

    path('import/', baza.Import.as_view(), name='import'),
    path('export/', baza.Export.as_view(), name='export'),

]
