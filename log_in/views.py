from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login #이름 부분은 자유
from django.contrib.auth import logout as auth_logout #이름 부분은 자유
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def first_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) #user대신 form.get_user()사용가능
            next_path = request.GET.get('next') or 'first_page'
            return redirect(next_path)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'log_in/first_page.html', context)

@require_POST
def log_out(request):
    auth_logout(request)
    return redirect("first_page")

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid:
        form.save()
        return redirect('first_page')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
        }
    return render(request, 'log_in/signup.html', context)