from django.shortcuts import render

# Create your views here.
from oscar.apps.catalogue.models import Product

def all_products(request):
    products = Product.objects.all()

    # print(products)
    # for p in products:
    #     print(p)
    
    context = {
        'products': products,
    }

    return render(request, 'all_products.html', context)