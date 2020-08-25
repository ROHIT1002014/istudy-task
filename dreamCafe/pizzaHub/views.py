from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def loginView(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return render(request, 'login.html')
  return render(request, 'login.html')

def logoutView(request):
  logout(request)
  return redirect('logout')

@login_required(login_url='login/')
def homePageView(request):
  return render(request, 'home.html', {'message': 'Login fail.'})