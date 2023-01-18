from django.db.migrations import serializer
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api import models, serializers
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(['GET'])
def get_products(request, *args, **kwargs):
    products = models.Product.objects.all()
    data = serializers.ProductModelSerializer(products, many=True).data
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def get_product(request, *args, **kwargs):
    # product = get_object_or_404(models.Product.objects.get(**kwargs))
    product = models.Product.objects.get(**kwargs)
    serializer = serializers.ProductModelSerializer(product)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_categories(request, *args, **kwargs):
    categories = models.Category.objects.all()
    data = serializers.CategoryModelSerializer(categories, many=True).data
    return JsonResponse(data,safe=False)

@api_view(['GET'])
def get_category(request, *args, **kwargs):
    category = models.Category.objects.get(**kwargs)
    serializer = serializers.CategoryModelSerializer(category)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_product_by_category_id(request, id):

    products = models.Product.objects.filter(category_id=id).all()
    serializer = serializers.ProductModelSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)
