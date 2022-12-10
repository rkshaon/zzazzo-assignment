from django import forms

from oscar.apps.catalogue.models import Product
from order_custom.models import Purchase
from user.models import User


class NewPurchaseForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        widget=forms.Select(attrs={
            'class': 'form-control',
        }), 
        required=True)
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), 
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        required=True)
    
    class Meta:
        model = Purchase
        fields = {
            'user', 'product'
        }