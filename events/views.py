from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Event
from .forms import EventForm
from django.contrib import messages
from .utils import ATTACH_AUTH_MESSAGE, ATTACH_OLD_USER_EVENTS_MESSAGE
from .data import *
from .manage_data import (
    STAGE_EXPIRED_EVENTS_FOR_DELETION,
    TOGGLE_STAGE_USER_EVENT_DELETE,
    DELETE_STAGED_EVENTS,
)

def search_events_view(request):
    context = {
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request),
    }
    if request.method == 'POST':
        q = request.POST.get('q')
        search_results = Event.objects.filter(
            Q(headliner__contains=q) | 
            Q(venue__contains=q) | 
            Q(description__contains=q) |
            Q(address_borough__contains=q)).values()
        if search_results.count() == 0:
            search_results = None
            context['num_search_results'] = 0
            context['search_results_message'] = 'There are no results for ' + f'"{q}."'
        else:
            context['num_search_results'] = search_results.count()
            if search_results.count() > 1:
              context['search_results_message'] = 'Showing ' + f'{search_results.count()}' + ' results for ' + f'"{q}."'
            else:
               context['search_results_message'] = 'Showing 1 result for ' + f'{q}.'
        context['q'] = q
        context['search_results'] = search_results
        return render(request, 'home.html', context=context)
    elif request.method == 'GET':
        return render(request, 'home.html', context=context)

def home(request):
    STAGE_EXPIRED_EVENTS_FOR_DELETION()
    DELETE_STAGED_EVENTS()
    context = {
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request),
        'num_expired_events': NUM_EXPIRED_EVENTS(),
    }
    ATTACH_AUTH_MESSAGE(request, context)
    return render(request, 'home.html', context=context)

def event_list_today_view(request):
    STAGE_EXPIRED_EVENTS_FOR_DELETION()
    DELETE_STAGED_EVENTS()
    context = {
        'todays_events': TODAYS_EVENTS(),
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }
    return render(request, 'home.html', context=context)

def event_list_week_view(request):
    STAGE_EXPIRED_EVENTS_FOR_DELETION()
    DELETE_STAGED_EVENTS()
    context = {
        'weeks_events': WEEKS_EVENTS(),
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }
    return render(request, 'home.html', context=context)

def event_list_upcoming_view(request):
    STAGE_EXPIRED_EVENTS_FOR_DELETION()
    DELETE_STAGED_EVENTS()
    context = {
        'upcoming_events': UPCOMING_EVENTS(),
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }
    return render(request, 'home.html', context=context)


def event_list_user_view(request):
    STAGE_EXPIRED_EVENTS_FOR_DELETION()
    DELETE_STAGED_EVENTS()
    context = {
        'user_events': USER_EVENTS(request),
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }
    ATTACH_AUTH_MESSAGE(request, context)

    num_old_user_events = NUM_USER_EVENTS_STAGED_FOR_DELETION(request)
    ATTACH_OLD_USER_EVENTS_MESSAGE(num_old_user_events, context)
    
    if request.user.is_authenticated:
      if NUM_USER_EVENTS(request) < 1: return redirect('/event_add/')
      return render(request, 'home.html', context=context)
    else:
      return redirect('/users/login_user?next=/my_events')

def add_event(request):
    context = {
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Listing added successfully.'))
            return redirect('event-list-user')
    elif request.method == 'GET':
        form = EventForm(initial={'owner': request.user})
    context['form'] = form
    if request.user.is_authenticated:
      ATTACH_AUTH_MESSAGE(request, context)
      return render(request, 'events/event_add.html', context=context)
    else:
      return redirect('/users/login_user?next=/event_add')

def update_event(request, event_id):
    context = {
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }  
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None,  instance=event)
    context['event'] = event
    if form.is_valid():
        form.save()
        return redirect('event-list-user')
    context['form'] = form
    return render(request, 'events/event_update.html', context=context)

def toggle_user_event_delete(request, event_id):
    TOGGLE_STAGE_USER_EVENT_DELETE(request, event_id)
    event = Event.objects.get(pk=event_id)
    if event.date < EVENT_EXPARATION_DATE:
      return redirect(f'/event_update/{event_id}')
    return redirect(f'event-list-user')
