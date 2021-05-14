from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'crm_app/index.html')


def products(request):
    return render(request, 'crm_app/products.html')


def customer(request):
    return render(request, 'crm_app/customer.html')