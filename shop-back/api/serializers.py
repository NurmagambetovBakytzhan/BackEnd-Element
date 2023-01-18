from rest_framework import serializers

from api import models


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    amount = serializers.IntegerField()
    is_active = serializers.BooleanField()
    category = serializers.IntegerField()

class ProductModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    amount = serializers.IntegerField()
    is_active = serializers.BooleanField()

    class Meta:
        model = models.Product
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

class CategoryModelSerializer(serializers.Serializer):
    name = serializers.CharField()
    class Meta:

        model = models.Category
        fields = '__all__'