from django.db import models
from django.conf import settings
from events.models import Event

class RSVP(models.Model):
    STATUS_CHOICES = (
        ('Going', 'Going'),
        ('Maybe', 'Maybe'),
        ('Decline', 'Decline'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.username} - {self.event.title} - {self.status}'

