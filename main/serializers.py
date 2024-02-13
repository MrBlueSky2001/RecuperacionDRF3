from .models import Post, Valoracion
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ValoracionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'
