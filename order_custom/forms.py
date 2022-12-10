from django import forms

from oscar.apps.catalogue.models import Product
from order_custom.models import Purchase
from order_custom.models import Payment
from user.models import User


class NewPurchaseForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        widget=forms.Select(attrs={
            'class': 'form-control',
        }), 
        required=True
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), 
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        required=True
    )
    
    class Meta:
        model = Purchase
        fields = {
            'user', 'product'
        }


class NewPaymentForm(forms.ModelForm):
    purchase = forms.ModelChoiceField(
        queryset=Purchase.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        required=True
    )
    amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'step': 0.25,
            'class': 'form-control',
        }),
        required=True
    )

    class Meta:
        model = Payment
        fields = {
            'purchase',
            'amount',
        }