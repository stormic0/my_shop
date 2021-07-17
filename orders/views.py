from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from .models import Order, OrderItem
from cart.cart import Cart
from .tasks import order_created


class OrderCreate(View):

    @staticmethod
    @login_required
    def post(request):
        cart = Cart(request)
        cart_list = cart
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        order_created.delay(order.id)
        return render(request, 'orders/order/created.html', {'order': order, 'cart': cart_list})
