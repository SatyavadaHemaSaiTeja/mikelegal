from rest_framework import viewsets, decorators, status
from rest_framework.response import Response

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    @decorators.action(detail=False, methods=['GET'])
    def active_subscribers(self, request):
        active_subscribers = Subscriber.objects.get_active_subscribers()
        serializer = self.get_serializer(active_subscribers, many=True)
        return Response(serializer.data)

    @decorators.action(detail=False, methods=['GET'])
    def inactive_subscribers(self, request):
        unsubscribers = Subscriber.objects.get_inactive_subscribers()
        serializer = self.get_serializer(unsubscribers, many=True)
        return Response(serializer.data)

    @decorators.action(detail=True, methods=['PUT'])
    def deactivate_subscriber(self, request, pk=None):
        try:
            subscriber = self.get_object()
        except:
            return Response({"detail": "Subscriber not found."}, status=status.HTTP_404_NOT_FOUND)
        subscriber.deactivate()
        serializer = self.get_serializer(subscriber)
        return Response(serializer.data)
