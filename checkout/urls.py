from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('<order_number>/checkout_success/',
         views.checkout_success,
         name="checkout_success"),
    path('cache_checkout/',
         views.cache_checkout,
         name='cache_checkout'),
    path('delivery/',
         views.delivery,
         name='delivery'),
    path('wh/', webhook, name='webhook'),
]