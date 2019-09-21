from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['maker', 'model','year','price','image']

class DetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['maker', 'model','color','gear','year','milage','price','image']