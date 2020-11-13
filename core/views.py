from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DirectionPrice
from .serializers import DirectionPriceSerializer


class DirectionPriceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DirectionPriceSerializer

    def get_queryset(self):
        fly_from = self.request.query_params.get("fly_from")
        fly_to = self.request.query_params.get("fly_to")
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")
        passenger_amount = self.request.query_params.get("passenger_amount")
        return DirectionPrice.objects.get_ordered_by_price(
            fly_from, fly_to, date_from, date_to, passenger_amount)

    @action(methods=['GET'], detail=False)
    def get_cheapest_flight(self, request):
        fly_from = self.request.query_params.get("fly_from")
        fly_to = self.request.query_params.get("fly_to")
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")
        passenger_amount = self.request.query_params.get("passenger_amount")
        serializer = self.get_serializer(
            DirectionPrice.objects.get_cheapest_ticket(
                fly_from, fly_to, date_from, date_to, passenger_amount))
        return Response(serializer.data)
