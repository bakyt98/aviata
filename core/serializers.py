from rest_framework import serializers
from .models import DirectionPrice, Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"


class DirectionPriceSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()

    class Meta:
        model = DirectionPrice
        fields = '__all__'
