import requests
from django.db import models


class DirectionPriceManager(models.Manager):
    def get_cheapest_ticket(self, fly_from, fly_to, date_from,
                            date_to, passenger_amount):
        direction_price = DirectionPrice.objects.filter(
            city_from=fly_from, city_to=fly_to,
            date__gte=date_from, date__lte=date_to,
            available_place_amount__gte=passenger_amount).order_by('price').first()
        return direction_price


class DirectionPrice(models.Model):
    city_from = models.CharField(max_length=10)
    city_to = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    date = models.DateField()
    available_place_amount = models.PositiveIntegerField(default=0)

    objects = DirectionPriceManager()

    def __str__(self):
        return f"{self.city_from} - {self.city_to}: {self.price}"
