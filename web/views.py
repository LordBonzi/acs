from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from django.contrib import messages
from pprint import pprint
from .forms import UserRegForm, NewGuest

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

#def register(request):
#    if request.method == 'POST':
#        form = UserRegForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            messages.success(request, f'Account {username} created.')
#            return redirect('IndexView')
#    else:
#        form = UserRegForm()
#    
#    context = { 'form': form }
#    return render(request, 'reg/reg.html', context)        

@login_required
def UserInfo(request):
    return render(request, 'user/user.html')

@login_required
def NewGuestView(request):
    if request.method == 'POST':
        form = NewGuest(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created.')
            return redirect('IndexView')
            charset = list('ABCDEFGHJKLMNPQRSTUVWXYZ3789')
            length = 8
            code = get_random_string(length=length, allowed_chars=charset)    
    else:
        form = NewGuest()
    
    context = { 'my_form': form }
    return render(request, 'guest/new.html', context)  
    
    return HttpResponse(str(code))

@login_required
def ReturningGuest(request):
    return