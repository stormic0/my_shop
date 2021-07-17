from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from cart.forms import CartAddProductionForm


class ProductList(View):

    @staticmethod
    def get(request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products.filter(category=category)
        context = {
            'category': category,
            'categories': categories,
            'products': products
        }
        return render(request, 'shop/product/list.html', context)


class ProductDetail(View):

    @staticmethod
    def get(request, pk, slug):
        product = get_object_or_404(Product, id=pk, slug=slug, available=True)
        context = {'product': product, 'cart_product_form': CartAddProductionForm()}
        return render(request, 'shop/product/detail.html', context)
