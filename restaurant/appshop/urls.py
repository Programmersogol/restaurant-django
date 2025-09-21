from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('SingUp',views.SingUp,name="SingUp"),
    path('logins',views.logins,name="logins"),
    path('logouts',views.logouts,name="logouts"),
    path('update_user/',views.update_user,name="update_user"),
    path('update_password',views.update_password,name="update_password"),
    path('update_info/',views.update_info,name="update_info"),
    path('category/',views.category,name="category"),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart-item-count/', views.cart_item_count, name='cart_item_count'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('update-cart-item/', views.update_cart_item, name='update_cart_item'),
    path('remove-cart-item/', views.remove_cart_item, name='remove_cart_item'),
    path('search/',views.search,name="search"),
    path('about',views.about,name="about")



]
