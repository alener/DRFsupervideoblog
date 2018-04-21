from rest_framework import serializers
from .models import SuperVideoPost

class SuperVideoPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuperVideoPost
        fields = ('id','url','user', 'collection', 'title', 'description','goals',
        	'how_to','youtube_link','image_link','start','end','file'
        	)