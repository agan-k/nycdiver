from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Event
from .forms import EventForm
from .utils import (
    ATTACH_AUTH_MESSAGE,
    ATTACH_POSTED_MESSAGE,
    ATTACH_OLD_USER_EVENTS_MESSAGE, 
    ATTACH_SEARCH_RESULTS_MESSAGE,
    INITIAL_DATE_AND_TIME,
) 
from .data import *
from .manage_data import (
    STAGE_EXPIRED_EVENTS_FOR_DELETION,
    TOGGLE_STAGE_USER_EVENT_DELETE,
    DELETE_STAGED_EVENTS,
)
from .v_vanguard import (get_vanguard, vanguardURL)
from .smalls import (get_smalls, smallsURL)
from .mazie import (get_mazie, mazieURL)
from .icp import (get_icp, icpURL)
from .zincbar import (get_zincbar, zincbarURL)

print(INITIAL_DATE_AND_TIME('time'))

def populate(request):
    print('request: ', request.path)
    if request.user.username != 'k-agan':
        return render(request, 'home.html')
    if request.path == '/populate_vanguard/':
        get_vanguard(vanguardURL)
        return redirect('/')
    elif request.path == '/populate_smalls/':
        get_smalls(smallsURL)
        return redirect('/')
    elif request.path == '/populate_mazie/':
        get_mazie(mazieURL)
        return redirect('/')
    elif request.path == '/populate_icp/':
        get_icp(icpURL)
        return redirect('/')
    elif request.path == '/populate_zincbar/':
        get_zincbar(zincbarURL)
        return redirect('/')
    

def search_events_view(request):
    context = {
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request),
    }
    if request.method == 'POST':
        search_request = request.POST.get('search_request')
        search_results = Event.objects.filter(
            Q(headliner__icontains=search_request) | 
            Q(venue__icontains=search_request) | 
            Q(description__icontains=search_request) |
            Q(address_borough__icontains=search_request)).values()
        ATTACH_SEARCH_RESULTS_MESSAGE(search_results, search_request, context)
        return render(request, 'home.html', context=context)
    elif request.method == 'GET':
        return render(request, 'home.html', context=context)

def home(request):
    STAGE_EXPIRED_EVENTS_FOR_DELETION()
    DELETE_STAGED_EVENTS()
    context = {
        'all_events': EVENTS(),
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request),
        'num_expired_events': NUM_EXPIRED_EVENTS(),
    }
    ATTACH_AUTH_MESSAGE(request, context)
    return render(request, 'home.html', context=context)
import datetime
import pytz
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
    if request.user.username == 'k-agan' or request.user.username == 'admin-staging':
        context['vanguard'] = '/populate_vanguard'
        context['smalls'] = '/populate_smalls'
        context['mazie'] = '/populate_mazie'
        context['icp'] = '/populate_icp'
        context['zincbar'] = '/populate_zincbar'
    ATTACH_AUTH_MESSAGE(request, context)
    ATTACH_POSTED_MESSAGE(request, context)

    num_old_user_events = NUM_USER_EVENTS_STAGED_FOR_DELETION(request)
    ATTACH_OLD_USER_EVENTS_MESSAGE(num_old_user_events, context)

    if request.user.is_authenticated:
      if NUM_USER_EVENTS(request) < 1: return redirect('/event_add/')
      return render(request, 'home.html', context=context)
    else:
      return redirect('/users/login_user?next=/my_events')

def add_event(request):
    print(request)
    context = {
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request), 
    }
    if request.user.username == 'k-agan' or request.user.username == 'admin-staging':
        context['vanguard'] = '/populate_vanguard'
        context['smalls'] = '/populate_smalls'
        context['mazie'] = '/populate_mazie'
        context['icp'] = '/populate_icp'
        context['zincbar'] = '/populate_zincbar'
    if request.method == 'POST':
        event = Event(owner=request.user)
        form = EventForm(request.POST, instance=event)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('/my_events/?added')
    elif request.method == 'GET':
        form = EventForm(initial={
            'owner': request.user, 
            'date': INITIAL_DATE_AND_TIME('date'),
            'time_start': INITIAL_DATE_AND_TIME('time'),
            'time_end': INITIAL_DATE_AND_TIME('time'),
            })
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
        return redirect('/my_events/?updated')
    context['form'] = form
    return render(request, 'events/event_update.html', context=context)

def toggle_user_event_delete(request, event_id):
    TOGGLE_STAGE_USER_EVENT_DELETE(request, event_id)
    event = Event.objects.get(pk=event_id)
    if event.date < EVENT_EXPIRATION_DATE:
      return redirect(f'/event_update/{event_id}')
    return redirect(f'event-list-user')
