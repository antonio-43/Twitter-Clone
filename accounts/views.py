from django.http import HttpResponse
from django.shortcuts import render

from .user_flow_control import pick_user, login 
from .forms import UserCreationForm, ConfirmUser

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('<h1>User Created</h1>')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def log_user(request):
    if request.method == 'POST':
        form = ConfirmUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            word = form.cleaned_data['password']
            if pick_user(username=name, password=word):
                return HttpResponse('<h1>LogedIN</h1>')
    else:
        form = ConfirmUser()

    context = {'form': form}
    return render (request, 'accounts/login.html', context)
