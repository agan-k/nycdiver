from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from events.data import (
    NUM_USER_EVENTS, 
    NUM_TODAYS_EVENTS,
    NUM_WEEKS_EVENTS,
    NUM_UPCOMING_EVENTS,
)

def login_user(request):
    next = request.GET.get('next')
    print('here:', next)
    if next:
        redirect_page = next + '/?loggedin'
    else:
        redirect_page = '/?loggedin'
    context = {
        'next': next,
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
        'num_user_events': NUM_USER_EVENTS(request),
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('redirect_page', redirect_page)
            return redirect(redirect_page)
        else:
            messages.error(request, ('There was an error logging in. Try again.'))
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'authentication/login.html', context=context)
    
def logout_user(request):
    logout(request)
    return redirect('/?loggedout')

def register_user(request):
    form_requirements = {
       'username': ['username can have letters, digits and characters @ . + - _ only'],
       'password': [
           'Your password can’t be too similar to your other personal information.',
           'Your password must contain at least 8 characters.',
           'Your password can’t be a commonly used password.',
           'Your password can’t be entirely numeric.',
           ],
    }
    context = {
        'form_requirements': form_requirements,
        'num_todays_events': NUM_TODAYS_EVENTS(),
        'num_weeks_events': NUM_WEEKS_EVENTS(),
        'num_upcoming_events': NUM_UPCOMING_EVENTS(),
    }
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context['form'] = form
        context['fruit'] = 'banana'
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/?loggedin')
    elif request.method == 'GET':
        form = RegistrationForm()
        context['form'] = form  
    return render(request, 'authentication/register_user.html', context=context)