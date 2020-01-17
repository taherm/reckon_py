from django.urls import path

from reckon_app import views

urlpatterns = [
    path('', views.index, name='index'),
    
    
   
]