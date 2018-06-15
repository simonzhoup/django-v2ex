from django.urls import path
from v2ex import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]