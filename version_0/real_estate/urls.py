from django.urls import path
from . import views

app_name = 'real_estate'

urlpatterns = [
    path('', views.home, name='home'),
    path('du-an/', views.project_list, name='project_list'),
    path('du-an/<int:pk>/', views.project_detail, name='project_detail'),
]
