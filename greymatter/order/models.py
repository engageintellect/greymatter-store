
from django.contrib.auth.models import User
from django.db import models
from product.models import Product

class Order(models.Model):
	ORDERED = 'ordered'
	PAID = 'paid'
	SHIPPED = 'shipped'

	STATUS_CHOICES = [
		(ORDERED, 'Ordered'),
		(PAID, 'Paid'),
		(SHIPPED, 'Shipped'),
	]

	user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	address = models.CharField(max_length=255)
	postal_code = models.CharField(max_length=255)
	place = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	is_paid = models.BooleanField(default=False)
	paid_amount = models.IntegerField(default=0)
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ORDERED)

	class Meta:
		ordering = ['-created_at',]
	
	def get_total_price(self):
		if self.paid_amount:
			return f'{self.paid_amount / 100:.2f}'


		return 0

	stripe_token = models.CharField(max_length=255)
	stripe_charge_id = models.CharField(max_length=255)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
	price = models.IntegerField()
	quantity = models.IntegerField(default=1)

	def get_total_price(self):
		return f'{(self.price) / 100:.2f}'

