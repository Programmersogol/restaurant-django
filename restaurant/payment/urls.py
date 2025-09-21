from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create-order/', views.create_order_from_cart, name='create_order_from_cart'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('fake-payment/<int:order_id>/', views.fake_payment, name='fake_payment'),
]
