from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
from products.models import Product
# Create your models here.
class Cart(models.Model):
	ORDER_STATUS = [
		('A', 'Active'),
		('P', 'Payment Successful'),
		('S', 'Shipped'),
		('Z', 'Complete'),
		('0', 'Inactive'),
		('F', 'Payment Failed'),
	]
	status = models.CharField(max_length=1,choices=ORDER_STATUS,default='A')
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	create_date = models.DateTimeField(auto_now_add=True)
	def get_total(self):
		total = 0
		for cart_item in self.cart_items.all():
			total += cart_item.sub_total()
		return total

	def view(self):
		return self.cart_items.all()

	def __str__(self):
		return  self.user.email


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='cart_items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def sub_total(self):
		return (self.product.price * self.quantity)

	def __str__(self):
		return  "%s: %s x %s = %s" % (self.cart.user, self.product.price, self.quantity, self.sub_total())

