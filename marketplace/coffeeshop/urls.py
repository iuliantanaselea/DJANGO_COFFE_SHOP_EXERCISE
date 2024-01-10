from django.urls import path
from. import views

urlpatterns = [
    path("users/", views.user_list, name="user_list"),
    path("products/", views.product_list, name="product_list"),
    path("orders/", views.order_list, name="order_list"),
    path('home/', views.home, name='home'),
]