from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homePageView(request):
  return render(request, 'home.html', {'message': 'Login fail.'})