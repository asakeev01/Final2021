from rest_framework import serializers


from .models import Order, Delivery



class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = (
            'url', 'user', 'cart',
            'fname', 'lname', 'email',
            'order_id', 'address', 'delivery',
            'created', 'paid', 'total',
            )
        read_only_fields = (
            'user', 'cart', 'total',
             'order_id', 'created', 'total'
            )


class DeliverySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Delivery
        fields = ('name', )