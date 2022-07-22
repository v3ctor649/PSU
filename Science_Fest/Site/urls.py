
from .import views

from django.urls import path
urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.register,name='register'),
    path('participants/',views.participant,name='participants'),
]