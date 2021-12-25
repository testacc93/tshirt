from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home),
    path('savedetails/', views.AddCustomer, name='savedetails'),
    path('createorder/', views.CreateOrder, name='createorder'),
    path('ordersEndPointUrl/', views.ordersEndPointUrl, name='ordersEndPointUrl'),

    
]
# urlpatterns = [
#     path('', views.home),
#     path('output/', views.return_data)
# ]