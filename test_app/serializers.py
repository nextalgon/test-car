from rest_framework import serializers, fields
from .models import Cars, Clients, Orders, ExOrders


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    client = ClientsSerializer(read_only=True, many=True)
    car = CarsSerializer(read_only=True, many=True)

    class Meta:
        model = Orders
        fields = "__all__"


class ExOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExOrders
        fields = "__all__"


class TimeFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['timestamp', 'from_date', 'to_date']
