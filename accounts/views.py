from .models import *
from .serializers import *
from .permissions import *
from django.http import Http404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_list_or_404, get_object_or_404



class UserCreateAPIView(CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = UserCreateSerializer

class UpdateUser(RetrieveUpdateAPIView):
	permission_classes = [TestPerm]
	serializer_class = UserCreateSerializer

	def check_object_permissions(self, request, obj):
		if obj.email != request.user:
			print(request.user,obj.email)
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, format=None):
		# if not 'email' in request.data:
		# 	return Response("where is the stuff", status=status.HTTP_400_BAD_REQUEST)
		email =  request.data['email']
		user_obj = get_object_or_404(User, email=email)
		serializer = UserSerializer(user_obj, data=request.data)
		if not serializer.is_valid():
			return Response(status=status.HTTP_400_BAD_REQUEST)
		self.check_object_permissions(self.request, user_obj)
		serializer.save()
		return Response(serializer.data)


class ViewUser(APIView):
	permission_classes = [IsAuthenticated]
	def get(self,request,format=None):
	# 	if 'email' in request.data:
	# 		email =  request.data['email']
	# 		user_obj = get_object_or_404(User, email=email)
	# 		serializer = UserSerializer(user_obj)
	# 		self.check_object_permissions(self.request, user_obj)
	# 		return Response(serializer.data)
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		self.check_object_permissions(self.request, users)
		return Response(serializer.data)
	
from .serializers import UserLoginSerializer

class LoginUser(APIView):
	serializer_class = UserLoginSerializer
	permission_classes = [AllowAny]
	def post(self, request):
		my_data = request.data
		serializer = UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=status.HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)