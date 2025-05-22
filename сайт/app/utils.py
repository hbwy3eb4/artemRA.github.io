from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "app/index.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = []
    categories.append(product.category)
    cur_category = product.category
    while cur_category.parent:
        categories.append(cur_category.parent)
        cur_category = cur_category.parent
    categories.reverse()
    context = {"product": product, "categories": categories}
    return render(request, "app/product_details.html", context)