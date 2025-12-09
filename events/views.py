from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from .models import Event
from .forms import EventForm
from rsvp.models import RSVP

def is_admin(user):
    return user.is_authenticated and user.is_admin()

@login_required
def event_list(request):
    today = timezone.localdate()
    events = Event.objects.filter(date__gte=today).order_by('date')
    return render(request, 'events/list.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    existing_rsvp = None
    if request.user.is_authenticated:
        existing_rsvp = RSVP.objects.filter(user=request.user, event=event).first()
    return render(request, 'events/detail.html', {'event': event, 'existing_rsvp': existing_rsvp})

@login_required
@user_passes_test(is_admin)
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, 'Event created')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit.html', {'form': form, 'event': event})

@login_required
@user_passes_test(is_admin)
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted')
        return redirect('event_list')
    return render(request, 'events/delete_confirm.html', {'event': event})

@login_required
@user_passes_test(is_admin)
def event_rsvp_summary(request, pk):
    event = get_object_or_404(Event, pk=pk)
    going = RSVP.objects.filter(event=event, status='Going').count()
    maybe = RSVP.objects.filter(event=event, status='Maybe').count()
    decline = RSVP.objects.filter(event=event, status='Decline').count()
    return render(request, 'events/summary.html', {
        'event': event,
        'going': going,
        'maybe': maybe,
        'decline': decline,
    })
