from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'dashboard/hello.html', {'message': message})



from django.shortcuts import render, redirect
from .models import Sales, SalesProduct
from pprint import pp, pprint




def create_sale(request):
    if request.method == 'POST':
        print(request.POST)
        customer_name = request.POST['customer_name']
        location = request.POST['location']
        total_price = request.POST['total_price']
        
        sale = Sales.objects.create(customer_name=customer_name, location=location, total_price=total_price)
        
        product_names = request.POST.getlist('product_name[]')
        product_prices = request.POST.getlist('product_price[]')
        quantities = request.POST.getlist('quantity[]')
        
        for name, price, quantity in zip(product_names, product_prices, quantities):
            SalesProduct.objects.create(sales=sale, product_name=name, product_price=price, quantity=quantity)
        
        return redirect('create_sale')
    
    return render(request, 'create_sale.html')