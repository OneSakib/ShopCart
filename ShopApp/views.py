from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cat = Category.objects.get(id=1)
    products = Product.objects.filter(avilable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, avilable=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product, 'categories': categories, 'cart_product_form': cart_product_form})
