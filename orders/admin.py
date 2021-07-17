from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = 'product',
    extra = False


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated'
    list_filter = 'paid', 'created', 'updated'
    raw_id_fields = 'user',
    inlines = OrderItemInline,

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    def address(self, obj):
        return obj.user.address

    def postal_code(self, obj):
        return obj.user.postal_code

    def city(self, obj):
        return obj.user.city


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
    pass
