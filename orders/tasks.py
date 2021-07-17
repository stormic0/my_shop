from myshop.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.user.get_full_name()},\n\nYou have successfully placed an order. Your order ID is {order.id}'
    mail_send = send_mail(subject, message, 'admin@myshop.com', [order.user.email])
    return mail_send
