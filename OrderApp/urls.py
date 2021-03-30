from django.urls import path
from .views import (
     Add_to_Shoping_cart, cart_details, 
     cart_delete, OrderCart, Order_showing, 
     Order_Product_showing, user_oder_details, useroderproduct_details)

urlpatterns = [
     path('addingcart/<int:id>/', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
     path('cart_details/', cart_details, name='cart_details'),
     path('cart_delete/<int:id>', cart_delete, name='cart_delete'),
     path('oder_cart/', OrderCart, name='OrderCart'),
     path('orderlist/', Order_showing, name="orderlist"),
     path('OrderProduct/', Order_Product_showing, name="orderproduct"),
     path('OrderDetails/<int:id>/', user_oder_details, name="user_oder_details"),
     path('OrderProductDetails/<int:id>/<int:oid>/', useroderproduct_details, name="useroderproduct_details"),
]