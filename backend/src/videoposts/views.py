from .models import SuperVideoPost
from rest_framework import viewsets
from .serializers import SuperVideoPostSerializer


class SuperVideoPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SuperVideoPost.objects.all()
    serializer_class = SuperVideoPostSerializer

