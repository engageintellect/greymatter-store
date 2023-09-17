from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'status', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'place', 'phone', 'created_at', 'updated_at', 'is_paid', 'paid_amount', 'status']	
	list_filter = ['created_at', 'updated_at', 'is_paid', 'status']
	search_fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'place', 'phone']
	inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)