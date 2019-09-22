from cart.models import Cart
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.
from .models import Payment
import requests

class Generate(APIView):
	def get(self, request, format=None):
		cart = get_object_or_404(Cart, user=self.request.user, status='A')
		payment = Payment.objects.create(cart=cart,amount=250)
		if payment:
			baseurl = 'http://demo.hesabe.com/authpost'
			payload = {
			'MerchantCode': payment.merchantcode, 
			'Amount': payment.amount,
			'SuccessUrl': 'http://localhost:8001/payment/success/%s' % payment.token,
			'FailureUrl': 'http://localhost:8001/payment/failure/%s' % payment.token,
			}
			response = requests.post(baseurl, data=payload)
			hesabe = response.json()
			if hesabe['status'] == "success":
				token = hesabe['data']['token']
				payment_url = hesabe['data']['paymenturl'] + token
				print(payment_url)
				return Response(hesabe, status=status.HTTP_200_OK)
		Response({'status':'payment failed'}, status=status.HTTP_400_BAD_REQUEST)


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
