from django.db import models
from django import forms
import random
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()



#if category:
#	category_tuple = (''.join(category*2))
#else:
#	category_tuple = ('', '')

class Users(models.Model):
	class Meta:
		verbose_name_plural = 'Пользователи'

	username = models.CharField('ФИО', max_length=90)
	user_login = models.CharField('Логин', max_length=20)
	user_password = models.CharField('Пароль', max_length=20)
	user_phone = models.CharField('Телефон', max_length=12)
	user_email = models.EmailField('Email')

	def __str__(self) -> str:
		return super().__str__()





class Categories(models.Model):
	class Meta:
		verbose_name_plural = 'Категории'

	category_name = models.CharField('Название категории', max_length=50)

	def __str__(self) -> str:
			return super().__str__()







# class Item(models.Model):
# 	class Meta:
# 		verbose_name_plural = 'Товары'

# 	cur.execute("""SELECT category_name FROM shop_categories""")
# 	category = cur.fetchall()
# 	CATEGORY_TUPLE = []
# 	for el in category:
# 		CATEGORY_TUPLE.append(tuple(el*2)) 
# 	tuple(CATEGORY_TUPLE)
	
# 	item_title = models.CharField('Название товара', max_length=90)
# 	item_img = models.ImageField('Изображение', upload_to='static/img/')
# 	item_description = models.TextField('Описание товара')
# 	item_articul = models.CharField('Артикул', max_length=10)
# 	item_url = models.URLField('Ссылка')
# 	item_delivery_price = models.IntegerField('Цена доставки', default=0)
# 	item_category = models.CharField('Класс одежды', max_length=90, choices=CATEGORY_TUPLE)

# 	item_price_cny_xs = models.IntegerField('Цена в CNY (XS)', default=0)
# 	item_price_cny_s = models.IntegerField('Цена в CNY (S)', default=0)
# 	item_price_cny_m = models.IntegerField('Цена в CNY (M)', default=0)
# 	item_price_cny_l = models.IntegerField('Цена в CNY (L)', default=0)

# 	def __str__(self):
# 			return self.item_title
	



class KursCNY(models.Model):
	class Meta:
		verbose_name_plural = 'Курс CNY'

	kurs_cny = models.IntegerField('Курс CNY в RUB')

	def __str__(self) -> str:
			return super().__str__()





class Order(models.Model):
	class Meta:
		verbose_name_plural = 'Заказы'

	cur.execute("""SELECT order_num FROM shop_order""")
	all_results = cur.fetchall()


	orderer_fio = models.CharField("ФИО", max_length=50)
	order_item = models.CharField("Название товара", max_length=250)
	orderer_phone = models.CharField('Телефон', max_length=12)
	order_address = models.CharField("Адрес доставки", max_length=250)
	order_price = models.IntegerField("Цена товара")
	order_num = models.IntegerField("Номер заказа",)

	

		
	def __str__(self) -> str:
		return super().__str__()



class Sneakers(models.Model):
	class Meta:
		verbose_name_plural = '2 Кроссовки'
	
	snk_title = models.CharField('Название', max_length=90)
	snk_name = models.CharField('Доп название', max_length=255, default='')
	snk_description = models.TextField('Описание кроссовки')
	snk_articul = models.CharField('Артикул', max_length=10)
	snk_url = models.URLField('Ссылка')
	snk_category = models.CharField('Категория', max_length=90)

	snk_img_1 = models.ImageField('Изображение 1', upload_to='static/img/', null=True, default='')
	snk_img_2 = models.ImageField('Изображение 2', upload_to='static/img/', null=True, default='')
	snk_img_3 = models.ImageField('Изображение 3', upload_to='static/img/', null=True, default='')
	snk_img_4 = models.ImageField('Изображение 4', upload_to='static/img/', null=True, default='')
	snk_img_5 = models.ImageField('Изображение 5', upload_to='static/img/', null=True, default='')
	snk_img_6 = models.ImageField('Изображение 6', upload_to='static/img/', null=True, default='')
	snk_img_7 = models.ImageField('Изображение 7', upload_to='static/img/', null=True, default='')
	snk_img_8 = models.ImageField('Изображение 8', upload_to='static/img/', null=True, default='')

	snk_price_cny_33 = models.IntegerField('Размер 33', default=0)
	snk_price_cny_34 = models.IntegerField('Размер 34', default=0)
	snk_price_cny_35 = models.IntegerField('Размер 35', default=0)
	snk_price_cny_36 = models.IntegerField('Размер 36', default=0)
	snk_price_cny_37 = models.IntegerField('Размер 37', default=0)
	snk_price_cny_38 = models.IntegerField('Размер 38', default=0)
	snk_price_cny_39 = models.IntegerField('Размер 39', default=0)
	snk_price_cny_40 = models.IntegerField('Размер 40', default=0)
	snk_price_cny_41 = models.IntegerField('Размер 41', default=0)
	snk_price_cny_42 = models.IntegerField('Размер 42', default=0)
	snk_price_cny_43 = models.IntegerField('Размер 43', default=0)
	snk_price_cny_44 = models.IntegerField('Размер 44', default=0)
	snk_price_cny_45 = models.IntegerField('Размер 45', default=0)
	

	def __str__(self):
			return self.item_title

			


#   ---------------------------------------------   CLOTHES ----------------------------------------------------
class Clothes(models.Model):
	class Meta:
		verbose_name_plural = '1 Одежды'

	cur.execute("""SELECT category_name FROM shop_categories""")
	category = cur.fetchall()
	CATEGORY_TUPLE = []
	for el in category:
		CATEGORY_TUPLE.append(tuple(el*2)) 
	tuple(CATEGORY_TUPLE)
	
	cloth_title = models.CharField('Название одежды', max_length=90)
	cloth_name = models.CharField('Доп название', max_length=255, default='')
	cloth_description = models.TextField('Описание товара')
	cloth_articul = models.CharField('Артикул', max_length=10)
	cloth_url = models.URLField('Ссылка')
	cloth_category = models.CharField('Класс одежды', max_length=90, choices=CATEGORY_TUPLE)

	cloth_img_1 = models.ImageField('Изображение 1', upload_to='static/img/', null=True, default='')
	cloth_img_2 = models.ImageField('Изображение 2', upload_to='static/img/', null=True, default='')
	cloth_img_3 = models.ImageField('Изображение 3', upload_to='static/img/', null=True, default='')
	cloth_img_4 = models.ImageField('Изображение 4', upload_to='static/img/', null=True, default='')
	cloth_img_5 = models.ImageField('Изображение 5', upload_to='static/img/', null=True, default='')
	cloth_img_6 = models.ImageField('Изображение 6', upload_to='static/img/', null=True, default='')
	cloth_img_7 = models.ImageField('Изображение 7', upload_to='static/img/', null=True, default='')
	cloth_img_8 = models.ImageField('Изображение 8', upload_to='static/img/', null=True, default='')

	cloth_price_cny_xl = models.IntegerField('Размер XL', default=0)
	cloth_price_cny_xs = models.IntegerField('Размер XS', default=0)
	cloth_price_cny_s = models.IntegerField('Размер S', default=0)
	cloth_price_cny_m = models.IntegerField('Размер M', default=0)
	cloth_price_cny_l = models.IntegerField('Размер L', default=0)

	def __str__(self):
			return self.item_title
	
