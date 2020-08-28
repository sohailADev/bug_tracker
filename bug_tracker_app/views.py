from django.shortcuts import render,HttpResponseRedirect,reverse
from bug_tracker_app import forms
from bug_tracker_app import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
    
@login_required(login_url='login_page')
def index_view(request):
    all_tickets = models.TicketModel.objects.all()  
  
    return render(request,'dashboard.htm',{'all_tickets':all_tickets})

def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data   
                 
            user = authenticate(username=data['username'], password=data['password'])          
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home_page")))
      
    form = forms.LoginForm()
    return render(request,'login.htm',{'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))

@login_required(login_url='login_page')
def ticket_detail_view(request,ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)
    return render(request,'ticket_detail.htm',{'ticket':ticket})

@login_required(login_url='login_page')
def user_detail_view(request,user_name):   
    user = models.TicketModel.objects.filter(user_filed__username=user_name).first()
    all_tickets = models.TicketModel.objects.filter(user_filed__username=user_name)
    return render(request,'user_detail.htm',{'all_tickets':all_tickets,'user':user})


@login_required(login_url='login_page')
def add_ticket_view(request):
    if request.method == 'POST':
        form = forms.AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data            
            new_ticket = models.TicketModel.objects.create(
                title = data['title'],
                description =data['description'],
                status = "New",
                user_assigned = None,
                user_ticket_completed = None,
                user_filed = request.user
                 )
            if new_ticket:
              return HttpResponseRedirect(reverse('home_page')) 
            

    form = forms.AddTicketForm()
    return render(request,'add_ticket.htm',{'form':form})
@login_required(login_url='login_page')
def edit_ticket_view(request,ticket_id):
    edit_ticket = models.TicketModel.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = forms.AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit_ticket.title = data['title']            
            edit_ticket.description = data['description']            
            edit_ticket.save()
            return HttpResponseRedirect(reverse('ticket_detail_page',args=(edit_ticket.id,)) ) 
            
    data = {'title':edit_ticket.title,'description':edit_ticket.description}
    form = forms.AddTicketForm(initial=data)
    return render(request,'edit_ticket.htm',{'form':form})
@login_required(login_url='login_page')
def assign_me_view(request,ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)  
    ticket.status = "In Progress"
    ticket.user_assigned = ticket.user_filed
    ticket.user_ticket_completed = None
    ticket.save()
    messages.success(request, "Assign to :" + str(ticket.user_filed))
    return HttpResponseRedirect(reverse('ticket_detail_page',args=(ticket.id,)) ) 
            
    
@login_required(login_url='login_page')   
def invalid_ticket_view(request,ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)  
    ticket.status = "Invalid"
    ticket.user_assigned = None
    ticket.user_ticket_completed = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_page',args=(ticket.id,))) 

        
        
@login_required(login_url='login_page')         
def complete_ticket_view(request,ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)  
    ticket.status = 'Done'
    ticket.user_assigned = None
    ticket.user_ticket_completed = ticket.user_filed
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_page',args=(ticket.id,)))  

@login_required(login_url='login_page')   
def return_ticket_view(request,ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)  
    ticket.status = "New"
    ticket.user_assigned = None
    ticket.user_ticket_completed = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_page',args=(ticket.id,)))  