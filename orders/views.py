from django.shortcuts import render
from rest_framework.views import  APIView
from cart.models import CartItem,Cart
from rest_framework.response import Response
from .models import Order
from rest_framework.generics import ListAPIView
from .models import Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class PlaceOrder(APIView):
    def post(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        items = CartItem.objects.filter(cart=cart)

        total = sum([item.product.price * item.quantity for item in items])

        #fake payment success
        payment_success = True

        if payment_success:
            order = Order.objects.create(user=user, total_amount = total)

            # reduce stock
            for item in items:
                item.product.stock -= item.quantity
                item.product.save()

            item.delete()

            return Response({"message": "Order placed", "total": total})
        return Response({"message": "Payment failed"})
    
class OrderHistory(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class UpdateOrderStatus(APIView):
    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        order.status = request.data.get("status")
        order.save()
        return Response({"message": "Update"})