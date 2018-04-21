from .models import Collection
from rest_framework import viewsets
from .serializers import PostCollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Collection.objects.all()
    serializer_class = PostCollectionSerializer