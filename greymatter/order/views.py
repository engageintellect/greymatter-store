from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Order, OrderItem

def start_order(request):
	cart = Cart(request)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		address = request.POST.get('address')
		postal_code = request.POST.get('postal_code')
		place = request.POST.get('place')
		phone = request.POST.get('phone')

		order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, address=address, postal_code=postal_code, place=place, phone=phone)	

		for item in cart:
			product = item['product']	
			quantity = int(item['quantity'])
			price = product.price * quantity

			item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)	

		return redirect('myaccount')
	return redirect('cart')

		
