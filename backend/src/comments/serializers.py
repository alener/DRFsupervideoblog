from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','url','super_video_post','user','body','timestamp' )