from rest_framework import generics
from rest_framework.response import Response
from django.db.models import F
from .models import Advert
from .serializers import AdvertListSerializer, AdvertDetailSerializer

class AdvertListView(generics.ListAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertListSerializer

class AdvertDetailView(generics.RetrieveAPIView):
    queryset = Advert.objects.select_related('city', 'category').all()
    serializer_class = AdvertDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views = F('views') + 1
        instance.save(update_fields=['views'])
        instance.refresh_from_db()
        return Response(self.get_serializer(instance).data)
