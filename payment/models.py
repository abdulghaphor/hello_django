from django.db import models
from cart.models import Cart
# Create your models here.
class Payment(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='payment')
	merchantcode = models.IntegerField(default=642616)
	amount = models.PositiveIntegerField()
	token = models.IntegerField(default=10000)
	status = models.CharField(max_length=1,null=True,blank=True)
	payment_token = models.CharField(max_length=20,null=True,blank=True)
	payment_id = models.CharField(max_length=20,null=True,blank=True)
	paid_on = models.CharField(max_length=20,null=True,blank=True)
	method = models.CharField(max_length=1,null=True,blank=True)
	administative_charge = models.CharField(max_length=20,null=True,blank=True)
	
	def __str__(self):
		return  "%s: %s x %s = %s" % (self.cart.user, self.product.price, self.quantity, self.sub_total())


# Status=1&
# PaymentToken=641569175678&
# PaymentId=100201926562131678&
# PaidOn=2019-09-22+21%3A09%3A33&
# Variable1=&
# Variable2=&
# Variable3=&
# Variable4=&
# Variable5=&
# Method=1&
# AdministrativeCharge=0

# Status - Payment status (1 - success 0 - failure )
# PaymentToken - Referance id
# PaymentId - Payment id
# PaidOn - Date time
# Variable1 - Custom user parameter 1
# Variable2 - Custom user parameter 2
# Variable3 - Custom user parameter 3
# Variable4 - Custom user parameter 4
# Variable5 - Custom user parameter 5
# Method=1 or 2 (KNET=1 and MIGs =2)