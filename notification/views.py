from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import *
from .models import Notification
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.
class NotificationHandler(APIView):
	permission_classes = [IsAuthenticated]
	serializer_class = NotificationSerializer
	def get(self, request, format=None):
		notifications = get_list_or_404(Notification, user=request.user)
		serializer = Notification(notifications,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)