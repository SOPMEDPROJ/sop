from django.contrib import admin
from django.utils.safestring import *
from .models import * 


# class ItemAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'get_img', 'item_category', 'item_articul', 'item_title', 'item_price_cny_xs', 'item_price_cny_s', 'item_price_cny_m', 'item_price_cny_l', 'item_delivery_price')
# 	list_display_links = ('id', 'get_img', 'item_category', 'item_articul', 'item_title')
# 	search_fields = ('item_category', 'item_articul', 'item_title')
# 	fields = ('item_img', 'get_img', 'item_category', 'item_articul', 'item_title', 'item_url', 'item_price_cny_xs', 'item_price_cny_s', 'item_price_cny_m', 'item_price_cny_l', 'item_delivery_price')
# 	readonly_fields = ('id', 'get_img')
	

# 	def get_img(self, object):
# 		return mark_safe(f"<img src='{object.item_img.url}' width=100'>")

# 	get_img.short_description = 'Изображение'



class KursCNYAdmin(admin.ModelAdmin):
	list_display = ('id', 'kurs_cny')
	list_display_links = ('id', 'kurs_cny')



class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('id', 'category_name')
	list_display_links = ('id', 'category_name')



class UsersAdmin(admin.ModelAdmin):
	list_display = ('id', 'user_login', 'username', 'user_password', 'user_phone', 'user_email')
	list_display_links = ('id', 'user_login', 'username')


class OrdersAdmin(admin.ModelAdmin):
	list_display = ('id', 'order_num', 'order_item', 'orderer_fio', 'order_price', 'order_address', 'orderer_phone')
	list_display_links = ('id', 'order_num', 'order_item')
	readonly_fields = ('order_num',)

class SneakersAdmin(admin.ModelAdmin):
	list_display = ('id', 'get_img', 'snk_title', 'snk_name', 'snk_category','snk_articul', 'snk_url', 
					'snk_price_cny_33', 
					'snk_price_cny_34', 
					'snk_price_cny_35', 
					'snk_price_cny_36',
					'snk_price_cny_37',
					'snk_price_cny_38',
					'snk_price_cny_39',
					'snk_price_cny_40',
					'snk_price_cny_41',
					'snk_price_cny_42',
					'snk_price_cny_43',
					'snk_price_cny_44',
					'snk_price_cny_45')
	list_display_links = ('id', 'get_img', 'snk_title', 'snk_name')
	search_fields = ('id', 'snk_title', 'snk_name', 'snk_articul')
	fields = ('get_img', 'snk_title', 'snk_name', 'snk_articul','snk_category', 'snk_url',
					'snk_price_cny_33', 
					'snk_price_cny_34', 
					'snk_price_cny_35', 
					'snk_price_cny_36',
					'snk_price_cny_37',
					'snk_price_cny_38',
					'snk_price_cny_39',
					'snk_price_cny_40',
					'snk_price_cny_41',
					'snk_price_cny_42',
					'snk_price_cny_43',
					'snk_price_cny_44',
					'snk_price_cny_45',
					'snk_img_1',
					'snk_img_2',
					'snk_img_3',
					'snk_img_4',
					'snk_img_5',
					'snk_img_6',
					'snk_img_7',
					'snk_img_8',)
	readonly_fields = ('id', 'get_img')
	

	def get_img(self, object):
		return mark_safe(f"<img src='{object.snk_img_1.url}'style='border-radius:50%' width=50'>")

	get_img.short_description = 'Изображение'

class ClothAdmin(admin.ModelAdmin):
	list_display = ('id', 'get_img', 'cloth_title', 'cloth_name', 'cloth_category','cloth_articul', 'cloth_url', 
					'cloth_price_cny_xl', 
					'cloth_price_cny_xs', 
					'cloth_price_cny_s', 
					'cloth_price_cny_m',
					'cloth_price_cny_l',)
	list_display_links = ('id', 'get_img', 'cloth_title', 'cloth_name')
	search_fields = ('id', 'cloth_title', 'cloth_name', 'cloth_articul')
	fields = ('', 'get_img', 'cloth_title', 'cloth_name', 'cloth_articul','cloth_category', 'cloth_url', 
					'cloth_price_cny_xl', 
					'cloth_price_cny_xs', 
					'cloth_price_cny_s', 
					'cloth_price_cny_m',
					'cloth_price_cny_l',
					'cloth_img_1',
					'cloth_img_2',
					'cloth_img_3',
					'cloth_img_4',
					'cloth_img_5',
					'cloth_img_6',
					'cloth_img_7',
					'cloth_img_8',)
	readonly_fields = ('id', 'get_img')
	

	def get_img(self, object):
		return mark_safe(f"<img src='{object.cloth_img_1.url}'style='border-radius:50%' width=50'>")

	get_img.short_description = 'Изображение'


# admin.site.register(Item, ItemAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(KursCNY, KursCNYAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Clothes, ClothAdmin)
admin.site.register(Sneakers, SneakersAdmin)


admin.site.site_title = 'Админ-панель | SAINT OFF PRICE'
admin.site.site_header = 'Админ-панель | SAINT OFF PRICE'