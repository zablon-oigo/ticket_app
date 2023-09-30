from django.shortcuts import render,redirect
from django.contrib import messages
import datetime
from .models import Ticket
from .forms import CreateTicketForm,UpdateTicketForm
from users.models import User
# view ticket details
def ticket_detail(request,pk):
    ticket=Ticket.objects.get(pk=pk)
    t=User.objects.get(username=ticket.created_by)
    tickets_per_user=t.created_by.all()
    return render(request,'ticket/ticket_details.html',{'ticket':ticket,'tickets_per_user':tickets_per_user})

""" For Customers"""
# create a ticket
def create_ticket(request):
    if request.method =='POST':
        form=CreateTicketForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.created_by=request.user
            var.ticket_status='Pending'
            var.save()
            messages.info(request,'Your ticket has been successfully submited an Engineer will be assigned soon')
            return redirect('dashboard')
        else:
            messages.warning(request,'Please correct the following error')
            return redirect('create-ticket')
    else:
        form=CreateTicketForm()
        return render(request,'ticket/create_ticket.html',{'form':form})
    
# update a ticket
def update_ticket(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    if not ticket.is_resolved:
        if request.method =='POST':
            form=UpdateTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                messages.info(request,'Your ticket has been updated successfully submited and chabges made to Databse')
                return redirect('dashboard')
            else:
                messages.warning(request,'Please correct the following error')
                # return redirect('create-ticket')
        else:
            form=UpdateTicketForm(instance=ticket)
            return render(request,'ticket/update_ticket.html',{'form':form})
    else:
        messages.warning(request,'You cannot make any changes')
        return redirect('dashboard')

# all created tickets
def all_tickets(request):
    tickets=Ticket.objects.filter(created_by=request.user).order_by('-date_created')
    return render(request,'ticket/all_tickets.html',{'tickets':tickets})


""" For Engineers"""

# view tickets Queue
def ticket_queue(request):
    tickets=Ticket.objects.filter(ticket_status='Pending')
    return render(request,'ticket/ticket_queue.html',{'tickets':tickets})

# accept a ticket
def accept_ticket(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    ticket.assigned_to=request.user
    ticket.ticket_status='Active'
    ticket.accepted_date=datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket has been accepted please resolve as soon as possible !')
    return redirect('workspace')

# close a ticket
def close_ticket(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    ticket.is_resolved=True
    ticket.ticket_status='Completed'
    ticket.closed_date=datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket has been resolved')
    return redirect('ticket-queue')



# ticket engineer is workin on
def workspace(request):
    tickets=Ticket.objects.filter(assigned_to=request.user, is_resolved=False)
    return render(request,'ticket/workspace.html', {'tickets':tickets})


# all closed ticket
def all_closed_tickets(request):
    tickets=Ticket.objects.filter(assigned_to=request.user, is_resolved=True)
    return render(request,'ticket/all_close_ticket.html',{'tickets':tickets})























    


