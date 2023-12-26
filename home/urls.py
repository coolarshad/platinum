from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('submit_contact_form/', views.submit_contact_form, name='submit_contact_form'),
]