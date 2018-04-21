from .models import Comment
from rest_framework import viewsets
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


