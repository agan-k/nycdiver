from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('events_today/', views.event_list_today_view, name='event-list-today'),
  path('events_week/', views.event_list_week_view, name='event-list-week'),
  path('events_upcoming/', views.event_list_upcoming_view, name='event-list-upcoming'),
  path('my_events/', views.event_list_user_view, name='event-list-user'),
  path('search_events', views.search_events_view, name='search-events'),
  path('event_add/', views.add_event, name='event-add'),
  path('event_update/<event_id>', views.update_event, name='event-update'),
  # path('event_delete/<event_id>', views.delete_event, name='event-delete'),
  path('toggle_user_event_delete/<event_id>', views.toggle_user_event_delete, name='toggle-user-event-delete'),
  # path('delete_expired_events/', views.delete_expired_events),
]
