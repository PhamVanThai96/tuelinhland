from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("contact/", views.ContactCreateView.as_view(), name="contact-create"),
    path("newsletter/", views.NewsletterCreateView.as_view(), name="newsletter-create"),
]
