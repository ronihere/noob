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
    return render(request,'app/hood.html')

def glass(request):
    return render(request,'app/glass.html')

def shoe(request):
    # http://43.206.240.172:8000/restapi/prod1-list/ 
    responseObj = requests.get('http://43.206.240.172:8000/restapi/prod1-list/',data={'key': 'value'})
    # print("response :")
    # print(responseObj.encoding)
    response=responseObj.json()
    dict={}
    # print(type(response))
    i=0
    str_="key"
    for item in response:
        dict[str_+str(i)]=item
        i+=1
    new_dict = {}
    for item in dict:
        temp=[]
        for val in dict[item]:
            temp.append(dict[item][val])
        new_dict[item] = temp
    print(new_dict)
        
    
    
    
    return render(request,'app/shoe.html',{'response':new_dict})

def cap(request):
    return render(request,'app/cap.html')
