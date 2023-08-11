from .data import EXPIRED_EVENTS, EVENTS_STAGED_FOR_DELETION, EVENT_DELETION_DATE
from .models import Event

def stage_expired_events_for_deletion():
    for expired_event in EXPIRED_EVENTS():
        expired_event.staged_for_deletion = True
        expired_event.save()

def toggle_stage_user_event_delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    if event.owner==request.user.username:
        event.staged_for_deletion = not event.staged_for_deletion
        event.save()
    
def delete_staged_events():
    for event in EVENTS_STAGED_FOR_DELETION():
        if event.date < EVENT_DELETION_DATE:
            event.delete()

STAGE_EXPIRED_EVENTS_FOR_DELETION = lambda: stage_expired_events_for_deletion()
TOGGLE_STAGE_USER_EVENT_DELETE = lambda request, event_id: toggle_stage_user_event_delete(request, event_id)
DELETE_STAGED_EVENTS = lambda: delete_staged_events()
