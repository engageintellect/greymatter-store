import json
import stripe
from django.conf import settings
from django.http import JsonResponse

from cart.cart import Cart
from .models import Order, OrderItem

def start_order(request):
	cart = Cart(request)
	data = json.loads(request.body)
	total_price = 0

	items = []

	for item in cart:
		product = item['product']
		total_price += product.price * int(item['quantity'])

		items.append({
			'price_data': {
				'currency': 'usd',
				'product_data': {
					'name': product.name,
				},
				'unit_amount': product.price,
			},
			'quantity': int(item['quantity']),
		})


	stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
	session = stripe.checkout.Session.create(
		payment_method_types=['card'],
		line_items=items,
		mode='payment',
  	# automatic_tax={"enabled": True},
		success_url='http://www.shopgme.com/cart/success/',
		cancel_url='http://www.shopgme.com/cart/'
	)

	payment_intent = session.payment_intent

	
	order = Order.objects.create(
		user=request.user, 
		first_name=data['first_name'],
		last_name=data['last_name'], 
		email=data['email'], 
		address=data['address'], 
		postal_code=data['postal_code'], 
		place=data['place'], 
		phone=data['phone'],
		# payment_intent=payment_intent,
		paid_amount=total_price,
		is_paid=True,
		# paid=True
	)	


	for item in cart:
		product = item['product']	
		quantity = int(item['quantity'])
		price = product.price * quantity

		item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)	
	
	cart.clear()

	return JsonResponse({'session': session, 'order': payment_intent})


		
