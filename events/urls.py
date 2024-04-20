from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('populate_vanguard/', views.populate, name='populate-vanguard'),
  path('populate_smalls/', views.populate, name='populate-smalls'),
  path('populate_mazie/', views.populate, name='populate-mazie'),
  path('populate_icp/', views.populate, name='populate-icp'),
  path('populate_zincbar/', views.populate, name='populate-zincbar'),
  path('events_today/', views.event_list_today_view, name='event-list-today'),
  path('events_week/', views.event_list_week_view, name='event-list-week'),
  path('events_upcoming/', views.event_list_upcoming_view, name='event-list-upcoming'),
  path('my_events/', views.event_list_user_view, name='event-list-user'),
  path('search_events', views.search_events_view, name='search-events'),
  path('event_add/', views.add_event, name='event-add'),
  path('event_update/<event_id>', views.update_event, name='event-update'),
  path('toggle_user_event_delete/<event_id>', views.toggle_user_event_delete, name='toggle-user-event-delete'),
]
