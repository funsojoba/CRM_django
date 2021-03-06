from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .form import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def home(request):
    orders = Order.objects.all()
    last_five_order = orders
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers =customers.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status='Pending').count()
    context ={
        'orders':orders,
        'customers':customers,
        'last_five_order':last_five_order,
        'total_orders':total_orders,
        'total_customers':total_customers,
        'delivered':delivered,
        'pending':pending
    }
    return render(request, 'crm_app/index.html', context)


def products(request):
    product = Product.objects.all()
    return render(request, 'crm_app/products.html', {'product':product})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'total_order':total_order,}
    return render(request, 'crm_app/customer.html', context)


def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form, 'customer': customer}
    return render(request, 'crm_app/create_order.html', context)


def updateOrder(request, pk):
    orders = Order.objects.get(id=pk)
    form = OrderForm(instance=orders)

    if request.method =='POST':
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'orders':orders, 'form':form,}
    return render(request, 'crm_app/update_order.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'order':order}
    return render(request, 'crm_app/delete_order.html', context)


def register(request):
    forms = UserCreationForm()
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('home')

    context = {'forms': forms}
    return render(request, 'crm_app/register.html', context)

def login(request):

    context = {}
    return render(request, 'crm_app/login.html', context)
