from django.shortcuts import render

from .models import Product


# Create your views here.


def home(request):
    details = Product.objects.all().values('id', 'name', 'serialnumber', 'price',
                                           'category_id', 'category_id__name', 'category_id__description')
    return render(request, 'products_table.html', {'Details': details})
