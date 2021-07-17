from django.urls import path
from .views import *


app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create'),
]
