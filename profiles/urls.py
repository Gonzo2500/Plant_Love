from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name="profile"),
    path('orders/', views.order_history, name="order_history"),
    path('orders/<order_id>', views.order_details, name="order_details"),
]