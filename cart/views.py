from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from django.views import View
from .cart import Cart
from .forms import CartAddProductionForm


class CartAdd(View):

    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')


class CartRemove(View):

    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product_id = get_object_or_404(Product, id=product_id)
        cart.remove(product_id)
        return redirect('cart:cart_detail')


class CartDetail(View):

    @staticmethod
    def get(request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductionForm(initial={'quantity': item['quantity'], 'override': True})
        return render(request, 'cart/detail.html', {'cart': cart})
