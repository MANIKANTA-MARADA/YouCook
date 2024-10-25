from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Event list
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # Event detail
    path('create/', views.create_event, name='create_event'),  # Create event
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),  # Delete event
]
