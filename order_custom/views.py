from django.shortcuts import render

from oscar.apps.catalogue.models import Product
from order_custom.models import Purchase
from user.models import User

from order_custom.forms import NewPurchaseForm


def add_purchase(request):
    if request.method == 'POST':
        form = NewPurchaseForm(request.POST)

        if form.is_valid():
            user = User.objects.get(pk=request.POST.get('user'))
            product = Product.objects.get(pk=request.POST.get('product'))

            purchase = Purchase.objects.create(
                user=user,
                product=product
            )
    
    form = NewPurchaseForm()

    context = {
        'form': form,
    }

    return render(request, 'add_purchase.html', context)