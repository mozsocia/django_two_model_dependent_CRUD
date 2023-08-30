from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def hello_view(request):
    message = "Hello World Django"
    return render(request, 'dashboard/hello.html', {'message': message})


from django.shortcuts import render, redirect
from .forms import SalesForm, SalesProductForm
from .models import Sales, SalesProduct

def create_sale(request):
    if request.method == 'POST':
        sales_form = SalesForm(request.POST)
        product_forms = [SalesProductForm(request.POST, prefix=str(i)) for i in range(2)]

        if sales_form.is_valid() and all(form.is_valid() for form in product_forms):
            sale = sales_form.save()

            for form in product_forms:
                product = form.save(commit=False)
                product.sales = sale
                product.save()

            return redirect('create_sale')
    else:
        sales_form = SalesForm()
        product_forms = [SalesProductForm(prefix=str(i)) for i in range(2)]

    return render(request, 'create_sale.html', {'sales_form': sales_form, 'product_forms': product_forms})

