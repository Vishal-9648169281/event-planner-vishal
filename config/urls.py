from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('event_list')),
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('rsvp/', include('rsvp.urls')),
]
