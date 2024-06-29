from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
# Create your views here.
@login_required(login_url='login')
def homePage(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class CustomPasswordResetConfirmView(SuccessMessageMixin,PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

