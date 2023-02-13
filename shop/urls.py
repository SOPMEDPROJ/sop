from django.urls import path
from . import views


urlpatterns = [
	path('', views.shop),
	path('orders/', views.orders)
]