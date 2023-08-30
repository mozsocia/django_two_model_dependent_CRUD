from django import forms
from .models import Sales, SalesProduct

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['customer_name', 'location', 'total_price']

class SalesProductForm(forms.ModelForm):
    class Meta:
        model = SalesProduct
        fields = ['product_name', 'product_price', 'quantity']
