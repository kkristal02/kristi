from django.shortcuts import render

import kris

# Create your views here.
def index(request):
    context = {
        'title':'T', 
        }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'T - Каталог',
        
    }
    return render(request,'products/products.html')