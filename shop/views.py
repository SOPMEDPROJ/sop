from django.shortcuts import render
from .models import *

def shop(request):
	data = Sneakers.objects.all()
	cny = KursCNY.objects.all()

	
	#kurs = [i.kurs_cny for i in cny]
	#price_cny = [ i.item_price_cny for i in data]
	#price = kurs[0] * price_cny[0]

	return render(request, 'shop/index.html', {
		"data": data,
		#"cny_rub": str(price) + '₽',
	})

def orders(request):
	order = Order.objects.all()

	return render(request, 'shop/orders.html', {
		'orders': order
	})