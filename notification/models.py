from django.db import models
from cart.models import Cart
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()

# Create your models here.
class Notification(models.Model):
	STATUS = [
		('S', 'Sent'),
		('R', 'Read'),
		('D', 'Deleted'),
	]
	status = models.CharField(max_length=1,choices=STATUS,default='S')
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	message = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	def send(self):
		total = 0
		for cart_item in self.cart_items.all():
			total += cart_item.sub_total()
		return total

	def view(self):
		return self.cart_items.all()

	def __str__(self):
		return  self.user.email


@receiver(post_save, sender=Cart)
def send_buy(sender, created, instance, **kwargs):
	if instance.status == 'P':
		message = 'Thank you for paying %s from us!' % instance.get_total()
		Notification.objects.create(user=instance.user,message=message)
