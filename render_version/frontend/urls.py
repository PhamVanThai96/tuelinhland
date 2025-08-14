from django.urls import path
from . import views

app_name = "frontend"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("properties/", views.property_list_view, name="property-list"),
    path("properties/<int:pk>/", views.property_detail_view, name="property-detail"),
    path("contact/", views.contact_view, name="contact"),
]
