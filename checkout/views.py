from django.shortcuts import render

# Create your views here. 
def view_checkout(request): 
    return render(request,'chekout/out.html' )  
