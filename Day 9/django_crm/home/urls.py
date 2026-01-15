from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('base/',views.base),
    path('home/',views.home,name='home'),
    path('customer/', views.customers, name='customer'),
]