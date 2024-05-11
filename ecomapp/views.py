from django.shortcuts import render

# Create your views here.
def index(request):
    active_nav = 'home'
    return render(request,'index.html',{'active_nav': active_nav})

def cart(request):
    return render(request,'cart.html')

def shop(request):
    active_nav = 'shop'
    return render(request,'shop.html',{'active_nav': active_nav})

def product(request):
    return render(request,'product.html')