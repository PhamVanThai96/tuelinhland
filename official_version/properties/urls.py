from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('types/', views.PropertyTypeListView.as_view(), name='property-types'),
    path('', views.PropertyListView.as_view(), name='property-list'),
    path('featured/', views.FeaturedPropertyListView.as_view(), name='featured-properties'),
    path('<int:pk>/', views.PropertyDetailView.as_view(), name='property-detail'),
]
