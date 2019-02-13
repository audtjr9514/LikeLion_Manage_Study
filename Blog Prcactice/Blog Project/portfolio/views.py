from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    Ports = Portfolio.objects
    return render(request, 'portfolio.html', {'ports':Ports})

# Create your views here.
