from cart.models import Cart
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.
class Successful(APIView):
	def get(self, request, format=None):
		cart = get_object_or_404(Cart, user=self.request.user, status='A')
		cart.status = 'P'
		cart.save()
		return Response({'status':'payment successful'}, status=status.HTTP_200_OK)

class Failed(APIView):
	def get(self, request, format=None):
		cart = get_object_or_404(Cart, user=self.request.user, status='A')
		cart.status = 'F'
		cart.save()
		return Response({'status':'payment failed'}, status=status.HTTP_400_BAD_REQUEST)
