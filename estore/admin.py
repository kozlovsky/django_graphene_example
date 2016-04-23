from django.contrib import admin

from . import models

class CustomerCartInline(admin.TabularInline):
    model = models.CartItem
    extra = 1

class CustomerOrderInline(admin.TabularInline):
    model = models.Order
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country')
    fields = (('name', 'email', 'password'), ('country', 'address'))
    inlines = [CustomerCartInline, CustomerOrderInline]

class ProductCartInline(admin.TabularInline):
    model = models.CartItem
    extra = 1

class ProductOrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = (('name', 'price', 'quantity'),
              ('picture', 'description'), 'categories',)
    inlines = [ProductCartInline, ProductOrderItemInline]

class OrderItemInline(admin.TabularInline):
    fields = ('product', 'price', 'quantity')
    model = models.OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'customer', 'status')
    fields = (('customer', 'status', 'total_price'),
              ('date_shipped', 'date_delivered'))
    inlines = [OrderItemInline]

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Category)
