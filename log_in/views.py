from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login #이름 부분은 자유
from django.contrib.auth import logout as auth_logout #이름 부분은 자유
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.views.decorators.http import require_http_methods
from .forms import CustomUserUpdate, CustumUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def first_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) #user대신 form.get_user()사용가능
            return redirect('main_page/')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'log_in/first_page.html', context)

@require_POST
def log_out(request):
    auth_logout(request)
    return redirect("/")

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == "POST":
        form = CustumUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/main_page/')
    else:
        form = CustumUserCreationForm()
    context = {
        'form' : form
        }
    return render(request, 'log_in/signup.html', context)

def out_membership(request):
    return render(request, 'log_in/out_membership.html')

def out_member(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("/")

@login_required
@require_http_methods(['GET', 'POST'])
def login_edit(request):
    if request.method == 'POST':
        form1 = CustomUserUpdate(request.POST, instance=request.user)
        form2 = PasswordChangeForm(request.user, request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            update_session_auth_hash(request, form2.user)
            auth_logout(request)
            return redirect("/")
    else:
        form1 = CustomUserUpdate(instance = request.user)
        form2 = PasswordChangeForm(request.user)
        context = {'form1': form1, 'form2' : form2}
    return render(request, 'log_in/login_edit.html', context)
