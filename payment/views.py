from cart.models import Cart
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

# class Generate(APIView):
# 	def get(self, request, format=None):
# 		cart = get_object_or_404(Cart, user=self.request.user, status='A')
# 		baseurl = 'http://demo.hesabe.com/authpost'
# 		payload = {
# 		'MerchantCode': 642616, 
# 		'Amount': 10,
# 		'SuccessUrl': 'value2',
# 		'FailureUrl': 'value2',
# 		}

# 		url = "http://demo.hesabe.com/authpost?MerchantCode=642616&Amount=100&SuccessUrl=http://localhost:8000/success&FailureUrl=http://localhost:8000/failure"

# 		response = requests.post(baseurl, data=payload)
# 		print(response.json())
# 		return Response(response.json(), status=status.HTTP_200_OK)

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
