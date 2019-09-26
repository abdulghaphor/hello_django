from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

#WILL TRY OPTIMIZING BY USING MODELVIEWSET LATER
class CartHandler(APIView):
	permission_classes = [IsAuthenticated]
	serializer_class = CartItemSerializer
	def get(self, request, format=None):
		cart, created = Cart.objects.get_or_create(user=request.user,status='A')
		serializer = CartSerializer(cart)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def delete(self,request,format=None):
		cart, created = Cart.objects.get_or_create(user=request.user,status='A')
		if 'product' in request.data:
			cart_item = get_object_or_404(CartItem, cart=cart, product=request.data['product'])
			cart_item.delete()
			return Response("Cart Item Deleted.", status=status.HTTP_204_NO_CONTENT)
		else:
			cart.delete()
			return Response("Cart Deleted.", status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def post(self,request):
		print(request.data)
		serializer = CartItemSerializer(data=request.data,context={'request':request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def put(self,request,format=None):
		serializer = CartItemSerializer(data=request.data,context={'request':request})
		if serializer.is_valid():
			print(serializer)
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Checkout(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		cart = get_object_or_404(Cart,user=request.user,status='A')
		serializer = CheckoutSerializer(cart)
		return Response(serializer.data, status=status.HTTP_200_OK)


###LEGACY CODE
# #post
# class Add(CreateAPIView):
# 	permission_classes = [IsAuthenticated]
# 	serializer_class = CartItemSerializer

# #delete
# class Delete(DestroyAPIView):
# 	def delete(self,request,format=None):
# 		cart = get_object_or_404(Cart, user=self.request.user)
# 		if 'product' in request.data:
# 			cart_item = get_object_or_404(CartItem, cart=cart,product=request.data['product'])
# 			cart_item.delete()
# 			return Response("Success.", status=status.HTTP_204_NO_CONTENT)
# 		else:
# 			cart.delete()
# 			return Response("Whole Cart Deleted.", status=status.HTTP_204_NO_CONTENT)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #put
# class Edit(RetrieveUpdateAPIView):
# 	serializer_class = CartItemSerializer

# 	def get_object(self):
# 		product = self.request.data['product']
# 		cart = get_object_or_404(Cart, user=self.request.user)
# 		cart_item = get_object_or_404(CartItem, cart=cart,product=product)
# 		return cart_item

# #get
# class List(APIView):
# 	def get(self, request, format=None):
# 		cart, created = Cart.objects.get_or_create(user=request.user)
# 		serializer = CartSerializer(cart)
# 		return Response(serializer.data, status=status.HTTP_200_OK)