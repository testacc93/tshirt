from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Customer, Order, Tshirt
from tshirtapp import models

def home(request):
    return render(request, 'home.html')

def CreateOrder(request):
    tshirt = models.Tshirt.objects.get(tshirtid=str(request.POST['tshirtid']))
    print("the tshirt is", tshirt)
    tshirtId = request.POST['tshirtid']
    orderid = request.POST['orderid']
    qty = request.POST['qty']
    amount = request.POST['amount']
    customer = request.POST['name']
    models.Order.objects.create(tshirt=tshirt, orderid=orderid, customer=customer, amount=amount, qty=qty)    
    return JsonResponse("success", safe=False)

def ordersEndPointUrl(request):
    print(request)
    return JsonResponse("success", safe=False)
    

def AddCustomer(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    address = request.POST['address']
    models.Customer.objects.create(name=name, email=email, contact=contact, address=address)    

    return JsonResponse("success", safe=False)
    
# def return_data(request):
#     return HttpResponse('entered text:' + request.POST['name'])