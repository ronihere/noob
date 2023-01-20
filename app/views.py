from django.shortcuts import render
from .models import DealsOfTheDay
import requests

def home(request):
    products = DealsOfTheDay.objects.all()
    context = {'products':products}
    # print(products)
    return render(request,'app/home.html',context)

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'authenticate/login.html')

def customerregistration(request):
 return render(request, 'authenticate/customerregistration.html')

def checkout(request):
    
    return render(request, 'app/checkout.html')


def hood(request):
    response = requests.get('http://43.206.240.172:8000/restapi/prod4-list/').json()
    return render(request,'app/hood.html',{'response':response})
    

def glass(request):
    response = requests.get('http://43.206.240.172:8000/restapi/prod3-list/').json()
    return render(request,'app/glass.html',{'response':response})

def shoe(request):
    response = requests.get('http://43.206.240.172:8000/restapi/prod1-list/').json()
    return render(request,'app/shoe.html',{'response':response})

def cap(request):
    response = requests.get('http://43.206.240.172:8000/restapi/prod2-list/').json()
    return render(request,'app/anarkali.html',{'response':response})

def custom(request):
    return render(request,'app/Finalhtml.html')
