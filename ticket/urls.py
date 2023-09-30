from django.urls import path

from .views import *

urlpatterns=[
    path('tickets-details/<int:pk>/',ticket_detail,name='ticket-details'),
    path('create-ticket/', create_ticket, name='create-ticket'),
    path('update-ticket/<int:pk>/', update_ticket,name='update-ticket'),
    path('all-tickets/', all_tickets, name='all-tickets'),
    path('ticket-queue/', ticket_queue, name='ticket-queue'),
    path('accept-ticket/<int:pk>/', accept_ticket, name='accept-ticket'),
    path('close-ticket/<int:pk>/', close_ticket, name='close-ticket'),
    path('workspace/', workspace, name='workspace'),
    path('all-closed-tickets',all_closed_tickets, name='all-closed-tickets'),
]