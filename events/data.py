from .models import Event
from datetime import date, timedelta, datetime

EVENT_EXPARATION_DATE = date.today()
EVENT_DELETION_DATE = date.today() - timedelta(weeks=1)

# from .models import Event
# from datetime import date, timedelta, datetime
# import pytz

# current_time = datetime.now(pytz.timezone('America/New_York'))
# EVENT_EXPARATION_DATE = datetime.now(pytz.timezone('America/New_York'))
# EVENT_DELETION_DATE = current_time - timedelta(weeks=1)


TODAYS_EVENTS = lambda: Event.objects.filter(
    date=date.today()).all()
EVENTS = lambda: Event.objects.all()
USER_EVENTS = lambda request: Event.objects.filter(
    owner=request.user.username).all()
UPCOMING_EVENTS = lambda: Event.objects.filter(
    date__gt=date.today()).all()
WEEKS_EVENTS = lambda: Event.objects.filter(
    date__range=[date.today(), date.today() + timedelta(days=6)]).all()
EXPIRED_EVENTS = lambda: Event.objects.filter(
    date__lt=EVENT_EXPARATION_DATE).all()
EXPIRED_USER_EVENTS = lambda request: EXPIRED_EVENTS().filter(owner=request.user.username).all()
EVENTS_STAGED_FOR_DELETION = lambda: Event.objects.filter(
    staged_for_deletion=True).all()
USER_EVENTS_STAGED_FOR_DELETION = lambda request: EVENTS_STAGED_FOR_DELETION().filter(owner=request.user.username).all()

NUM_USER_EVENTS = lambda request : USER_EVENTS(request).count()
NUM_EVENTS = lambda : EVENTS().count()
NUM_TODAYS_EVENTS =  lambda : TODAYS_EVENTS().count()
NUM_WEEKS_EVENTS = lambda : WEEKS_EVENTS().count()
NUM_UPCOMING_EVENTS = lambda : UPCOMING_EVENTS().count()
NUM_EXPIRED_EVENTS = lambda : EXPIRED_EVENTS().count()
NUM_USER_EVENTS_STAGED_FOR_DELETION = lambda request: USER_EVENTS_STAGED_FOR_DELETION(request).count()
