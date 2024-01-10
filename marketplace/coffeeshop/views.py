from django.shortcuts import render
from .models import User, Product, Order, Home


# Create your views here.

def user_list(request):
    users = User.objects.all()  # extrage din baza de date toti utilizatorii
    return render(request, 'users.list.html', {'users': users})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.list.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders.list.html', {'orders': orders})
def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {"home": home})