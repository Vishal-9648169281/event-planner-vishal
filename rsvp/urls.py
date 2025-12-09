from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_pk>/submit/', views.submit_rsvp, name='submit_rsvp'),
    path('my/', views.my_rsvps, name='my_rsvps'),
]
