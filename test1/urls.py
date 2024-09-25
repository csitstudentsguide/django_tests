from django.urls import path
from . import views

urlpatterns = [
    path('', views.test1_home, name='test1_home'),
]