def attach_auth_message(request, context):
      if 'loggedin' in request.GET:
        context['auth_message'] = f'You are logged in as {request.user}.'
      elif 'loggedout' in request.GET:
        context['auth_message'] = f'Logged out successfully.'
          
ATTACH_AUTH_MESSAGE = lambda request, context: attach_auth_message(request, context)