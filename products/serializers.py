from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = ['id','manufacturer', 'model','color','gear','year','milage','price','image']
	def get_image(self, product):
		request = self.context.get('request')
		photo_url = product.image.url
		return request.build_absolute_uri(photo_url)

class DetailsSerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = ['id','manufacturer', 'model','color','gear','year','milage','price','image']
	def get_image(self, product):
		request = self.context.get('request')
		photo_url = product.image.url
		return request.build_absolute_uri(photo_url)