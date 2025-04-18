from django.urls import path
from . import views  # Импорт views из текущего приложения

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account_view, name='account'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('order/create/', views.create_order, name='create_order'),
    path('orders/', views.orders_view, name='orders_view'),
    path('order/success/', views.order_success, name='order_success'),
    path('cart/detail/', views.cart_detail, name='cart_detail'),
]
