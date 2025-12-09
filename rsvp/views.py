from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from events.models import Event
from .models import RSVP

@login_required
def submit_rsvp(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    today = timezone.localdate()
    if event.date < today:
        messages.error(request, 'You cannot change RSVP after event date.')
        return redirect('event_detail', pk=event.pk)

    if request.method == 'POST':
        status = request.POST.get('status')
        if status not in ['Going', 'Maybe', 'Decline']:
            messages.error(request, 'Invalid status.')
            return redirect('event_detail', pk=event.pk)

        rsvp, created = RSVP.objects.get_or_create(user=request.user, event=event)
        rsvp.status = status
        rsvp.save()
        messages.success(request, 'RSVP updated.')
    return redirect('event_detail', pk=event.pk)

@login_required
def my_rsvps(request):
    rsvps = RSVP.objects.select_related('event').filter(user=request.user).order_by('-updated_at')
    return render(request, 'rsvp/my_rsvp.html', {'rsvps': rsvps})
