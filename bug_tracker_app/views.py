from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request,'dashboard.htm')
    

def login_view(request):
    return render(request,'login.htm')
