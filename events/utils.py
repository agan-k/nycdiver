from datetime import datetime

current_dateTime = datetime.now()

'''
form.fields['tank'].initial = 123

'''

def initial_date_and_time(field_type):
   initial_date = datetime.now()
   initial_time = initial_date.replace(second=0)
   if field_type == 'date':
      return initial_date
   else:
      return initial_time

INITIAL_DATE_AND_TIME = lambda field_type: initial_date_and_time(field_type)

def attach_auth_message(request, context):
    if 'loggedin' in request.GET:
      context['auth_message'] = f'You are logged in as {request.user}.'
    elif 'loggedout' in request.GET:
      context['auth_message'] = f'Logged out successfully.'
def attach_posted_message(request, context):
    if 'added' in request.GET:
      context['posted_message'] = f'Event added successfully.'
    elif 'updated' in request.GET:
      context['posted_message'] = f'Event updated successfully.'

def attach_old_user_events_message(num_old_user_events, context):
   if num_old_user_events > 0:
        if num_old_user_events > 1:
            context['old_user_events_message'] = f'''
            There are {num_old_user_events} old events. 
            Old events will be deleted automatically after one week.
            '''
        elif num_old_user_events < 2:
            context['old_user_events_message'] = f'''
            There is 1 old event. Old events will be deleted 
            automatically after one week.
            '''
          
def attach_search_results_message(search_results, search_request, context):
    if search_results.count() == 0:
        search_results = None
        context['num_search_results'] = 0
        context['search_results_message'] = 'There are no results for ' + f'"{search_request}."'
    else:
        context['num_search_results'] = search_results.count()
        if search_results.count() > 1:
          context['search_results_message'] = 'Showing ' + f'{search_results.count()}' + ' results for ' + f'"{search_request}."'
        else:
          context['search_results_message'] = 'Showing 1 result for ' + f'"{search_request}."'
    context['search_results'] = search_results
    context['search_request'] = search_request
          
ATTACH_SEARCH_RESULTS_MESSAGE = lambda search_results, search_request, context : attach_search_results_message(search_results, search_request, context)
ATTACH_OLD_USER_EVENTS_MESSAGE = lambda old_user_events, context: attach_old_user_events_message(old_user_events, context)
ATTACH_AUTH_MESSAGE = lambda request, context: attach_auth_message(request, context)
ATTACH_POSTED_MESSAGE = lambda request, context: attach_posted_message(request, context)