def attach_auth_message(request, context):
      if 'loggedin' in request.GET:
        context['auth_message'] = f'You are logged in as {request.user}.'
      elif 'loggedout' in request.GET:
        context['auth_message'] = f'Logged out successfully.'

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
          
ATTACH_OLD_USER_EVENTS_MESSAGE = lambda old_user_events, context: attach_old_user_events_message(old_user_events, context)
ATTACH_AUTH_MESSAGE = lambda request, context: attach_auth_message(request, context)