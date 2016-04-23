from graphene import relay, ObjectType
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode

from . import models

class CustomerNode(DjangoNode):
    class Meta:
        model = models.Customer
        filter_fields = ['name', 'email']
        filter_order_by = ['name', 'email']

class CartItemNode(DjangoNode):
    class Meta:
        model = models.CartItem
        filter_fields = ['customer', 'product', 'quantity']
        filter_order_by = ['quantity']

class CategoryNode(DjangoNode):
    class Meta:
        model = models.Category
        filter_fields = ['name']
        filter_order_by = ['name']

class ProductNode(DjangoNode):
    class Meta:
        model = models.Product
        filter_fields = ['name', 'price', 'quantity']
        filter_order_by = ['name', 'price', 'quantity']

class OrderNode(DjangoNode):
    class Meta:
        model = models.Order
        filter_fields = ['date_created', 'date_shipped', 'date_delivered',
                         'total_price', 'customer']
        filter_order_by = ['total_price', 'date_created', 'date_shipped', 'date_delivered']

class OrderItemNode(DjangoNode):
    class Meta:
        model = models.OrderItem
        filter_fields = ['order', 'product', 'price', 'quantity']
        filter_order_by = ['price', 'quantity']


class Query(ObjectType):
    customer = relay.NodeField(CustomerNode)
    category = relay.NodeField(CategoryNode)
    product = relay.NodeField(ProductNode)
    order = relay.NodeField(OrderNode)

    cart_item = relay.NodeField(CartItemNode)
    order_item = relay.NodeField(OrderItemNode)

    all_customers = DjangoFilterConnectionField(CustomerNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_products = DjangoFilterConnectionField(ProductNode)
    all_orders = DjangoFilterConnectionField(OrderNode)

    class Meta:
        abstract = True
