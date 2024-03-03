from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_contact/', views.add_contact, name='add_contact'),
]
