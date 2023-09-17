from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review

def product(request, slug):
		product = get_object_or_404(Product, slug=slug)

		if request.method == 'POST':
			rating = request.POST.get('rating', 3)
			content = request.POST.get('content', '')

			print(rating, content)
			
			if content:
				reviews = Review.objects.filter(product=product, created_by=request.user)

				if reviews.count() > 0:
					review = reviews.first()
					review.rating = rating
					review.content = content
					review.save()
				else:
					review = Review.objects.create(
						product=product,
						rating=rating, 
						content=content,
						created_by=request.user,
					)

				return redirect('product', slug=slug)
		
		return render(request, 'product/product.html', {'product': product})