from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import *
from .permissions import *
from django.http import Http404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, ListAPIView, CreateAPIView,RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_list_or_404, get_object_or_404

#okay
#post method
#generates Token to keep logged in for frontend
class Register(CreateAPIView):
	permission_classes = [AllowAny]
	serializer_class = RegisterSerializer

#okay
#post method
#generates token
class Login(APIView):
	serializer_class = LoginSerializer
	permission_classes = [AllowAny]
	def post(self, request):
		my_data = request.data
		serializer = LoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=status.HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class ChangePassword(UpdateAPIView):
	serializer_class = ChangePasswordSerializer
	model = User
	permission_classes = (IsAuthenticated,)

	def get_object(self):
		return self.request.user

	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
		# Check old password
			if not self.object.check_password(serializer.data.get("old_password")):
				return Response({"old_password":"Wrong password."}, status=status.HTTP_400_BAD_REQUEST)
			# set_password also hashes the password that the user will get
			self.object.set_password(serializer.data.get("new_password"))
			self.object.save()
			return Response("Success.", status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get request
class Details(RetrieveAPIView):
	serializer_class = DetailsSerializer
	def get_object(self):
		return self.request.user

#put request
class Edit(RetrieveUpdateAPIView):
	serializer_class = DetailsSerializer
	def get_object(self):
		return self.request.user

#okay
class Delete(DestroyAPIView):
	serializer_class = DetailsSerializer
	def get_object(self):
		return self.request.user
	def delete(self):
		return Response("Success.", status=status.HTTP_204_NO_CONTENT)

class List(ListAPIView):
	queryset = User.objects.all()
	serializer_class = ListSerializer
	permission_classes = [AllowAny]	


