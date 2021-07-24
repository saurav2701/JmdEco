from django.shortcuts import render 
from .models import Products 

# Create your views here. 
def home(request): 
    return render(request,'mainweb/home.htm' ) 

def detail(request): 
    products = Products.objects.all()  
    return render(request, 'mainweb/proddetail.htm', {"products"  : products}) 

def twowheeler(request): 
    products = Products.objects.all()
    return render(request , 'mainweb/twowheeler.html' , {"products" : products }) 
     


