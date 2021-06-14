from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('<product_id>/add/',
         views.add_item_to_cart,
         name="add_item_to_cart"),
    path('<product_id>/change/',
         views.change_cart,
         name="change_cart"),
    path('<product_id>/remove/',
         views.remove_item_from_cart,
         name="remove_item_from_cart"),
]