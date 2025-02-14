from rest_framework import generics


from core.models import Current  # Import depuis core.models
from ..serializers import CurrentSerializer


class CurrentListAPIView(generics.ListAPIView):
    queryset = Current.objects.all()
    serializer_class = CurrentSerializer

