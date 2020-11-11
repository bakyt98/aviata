from rest_framework import serializers
from .models import DirectionPrice


class DirectionPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionPrice
        fields = '__all__'
