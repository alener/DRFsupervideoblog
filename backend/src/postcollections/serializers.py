from rest_framework import serializers
from .models import Collection

class PostCollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ('id','url','creator','title','goals','description')