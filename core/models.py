from django.db import models


class Direction(models.Model):
    city_from = models.CharField(max_length=10)
    city_to = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city_from} - {self.city_to}"


class DirectionPriceManager(models.Manager):
    def get_cheapest_ticket(self, fly_from, fly_to, date_from,
                            date_to, passenger_amount):
        direction_price = DirectionPrice.objects.filter(
            direction__city_from=fly_from, direction__city_to=fly_to,
            date__gte=date_from, date__lte=date_to,
            available_place_amount__gte=passenger_amount).order_by(
                'price', 'date').first()
        return direction_price

    def get_ordered_by_price(self, fly_from, fly_to, date_from,
                             date_to, passenger_amount):
        direction_prices = DirectionPrice.objects.filter(
            direction__city_from=fly_from, direction__city_to=fly_to,
            date__gte=date_from, date__lte=date_to,
            available_place_amount__gte=passenger_amount).order_by(
                'price', 'date')
        return direction_prices


class DirectionPrice(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE,
                                  related_name="prices")
    price = models.PositiveIntegerField(default=0)
    date = models.DateField()
    available_place_amount = models.PositiveIntegerField(default=0)

    objects = DirectionPriceManager()

    def __str__(self):
        return f"{self.direction}: {self.price}"
