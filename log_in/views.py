from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def first_page(request):
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'log_in/first_page.html', context)

def new_user(requset):
    return render(requset, 'log_in/new_user.html')

def log_in(request):
    return render(request, 'log_in/log_in.html')