from django.urls import path
from .views import UpdateOrderStatus

urlpatterns = [
    path('update/<int:pk>/', UpdateOrderStatus.as_view())
]