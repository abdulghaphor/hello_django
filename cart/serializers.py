from rest_framework import serializers
from .models import *

class CartItemSerializer(serializers.ModelSerializer):
	unit_price = serializers.CharField(read_only=True)
	sub_total = serializers.CharField(read_only=True)	
	quantity = serializers.IntegerField(default=1, initial=1)
	class Meta:
		model = CartItem
		fields = ['product','unit_price','quantity','sub_total']

	def create(self, validated_data):
		product = validated_data['product']
		quantity = validated_data['quantity']
		cart, created = Cart.objects.get_or_create(user=self.context['request'].user,status='A')
		cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product)
		if created or self.context['request'].method == 'PUT':
			cart_item.quantity = quantity
		else:
			cart_item.quantity += quantity
		cart_item.save()
		validated_data['quantity'] = cart_item.quantity
		validated_data['unit_price'] = product.price
		validated_data['sub_total'] = cart_item.sub_total()		
		return validated_data

class CartSerializer(serializers.ModelSerializer):
	cart_items = serializers.SerializerMethodField()
	total = serializers.SerializerMethodField()
	class Meta: 
		model = Cart
		fields = ['cart_items','total']
	def get_cart_items(self, obj):
		cartitem = obj.view()
		return CartItemSerializer(cartitem, many=True).data
	def get_total(self, obj):
		return obj.get_total()

class CheckoutSerializer(serializers.ModelSerializer):
	status = serializers.SerializerMethodField()
	cart_items = serializers.SerializerMethodField()
	total = serializers.SerializerMethodField()
	class Meta: 
		model = Cart
		fields = ['cart_items','total','status']
	def get_cart_items(self, obj):
		cartitem = obj.view()
		return CartItemSerializer(cartitem, many=True).data
	def get_total(self, obj):
		return obj.get_total()
	def get_status(self,obj):
		obj.status = 'P'
		obj.save()
		return obj.status

class HistorySerializer(serializers.ModelSerializer):
	status = serializers.SerializerMethodField()
	cart_items = serializers.SerializerMethodField()
	total = serializers.SerializerMethodField()
	class Meta: 
		model = Cart
		fields = ['cart_items','total','status']
	def get_cart_items(self, obj):
		cartitem = obj.view()
		return CartItemSerializer(cartitem, many=True).data
	def get_total(self, obj):
		return obj.get_total()
	def get_status(self,obj):
		return obj.status