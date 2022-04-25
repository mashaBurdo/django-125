from . import views
from django.urls import path

urlpatterns = [
    path('car/', views.Car,name='car'),
    path('info/', views.info,name='info'),
    path('', views.main,name='index'),
    path('bmw/',views.bmw,name='bmw'),
    path('volvo/',views.volvo,name='volvo'),
    path('tesla/',views.tesla,name='tesla'),
]