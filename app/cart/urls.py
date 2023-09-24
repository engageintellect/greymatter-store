from django.urls import path
from .views import add_to_cart, buy_now, cart, checkout, hx_menu_cart, update_cart, hx_cart_subtotal, hx_cart_total, hx_cart_tax, success

urlpatterns = [
	path('', cart, name='cart'),
	path('success/', success, name='success'),
	path('checkout/', checkout, name='checkout'),
	path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
	path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
	path('buy_now/<int:product_id>/', buy_now, name='buy_now'),
	path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
	path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
	path('hx_cart_subtotal/', hx_cart_subtotal, name='hx_cart_subtotal'),
	path('hx_cart_tax/', hx_cart_tax, name='hx_cart_tax'),

]