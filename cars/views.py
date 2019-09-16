
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.
class CarList(ListAPIView):
	permission_classes = [AllowAny]
	serializer_class = CarSerializer
	queryset = Car.objects.all()
