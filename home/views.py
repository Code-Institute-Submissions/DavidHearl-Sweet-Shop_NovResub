from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    products = Product.objects.filter(featured=True)

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
