
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class List(APIView):

	permission_classes = [AllowAny]
	def get(self, request, format=None):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

class Details(APIView):
	permission_classes = [AllowAny]

	def get(self, request, pk, format=None):
		product = self.get_object(pk)
		serializer = DetailsSerializer(product)
		return Response(serializer.data)

	def get_object(self,pk):
		return Product.objects.get(pk=pk)