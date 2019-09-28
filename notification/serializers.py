from rest_framework import serializers
from .models import *


class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = ['create_date','message','status']