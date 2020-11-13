import requests
from celery import shared_task
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings

from .models import Direction, DirectionPrice

@shared_task
def update_prices():
    try:
        date_today = date.today()
        date_after_month = date_today + relativedelta(months=1)
        date_from = date_today.strftime("%d/%m/%Y")
        date_to = date_after_month.strftime("%d/%m/%Y")
        for direction in Direction.objects.all():
            response = requests.get(
                f"{settings.GET_FLIGHTS_URL}?fly_from={direction.city_from}&fly_to={direction.city_to}&date_from={date_from}&date_to={date_to}&partner=picky")
            for flight in response.json()['data']:
                booking_token = flight['booking_token']
                flights_checked = False
                new_price = flight['price']
                flights_invalid = False
                while not flights_checked:
                    content = requests.get(
                        f"{settings.FLIGHTS_CHECK_URL}&booking_token={booking_token}&bnum=0&pnum=1").json()
                    flights_checked = content['flights_checked']
                    flights_invalid = content['flights_invalid']
                    if flights_checked and content['price_change']:
                        new_price = content['tickets_price']
                if (flight['availability']['seats'] or 0) > 0 and not flights_invalid:
                    direction_price, _ = DirectionPrice.objects.get_or_create(
                        direction_id=direction.id,
                        date=datetime.fromtimestamp(flight['dTime']))
                    direction_price.price = new_price
                    direction_price.available_place_amount = flight['availability']['seats']
                    direction_price.save()
    except Exception as e:
        print(str(e))
