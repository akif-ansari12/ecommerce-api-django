from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart,CartItem
from products.models import Product


class AddToCart(APIView):
    def post(self, request):
        user = request.user
        product_id = request.data.get("product_id")
        quantity = request.data.get("qauntity", 1)

        cart,_ = Cart.objects.get_or_create(user=user)
        product = Product.objects.get(id=product_id)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += int(quantity)
        item.save()

        return Response({"message": "Added to cart"})


