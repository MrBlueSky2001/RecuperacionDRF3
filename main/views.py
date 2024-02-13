# Create your views here.
from rest_framework import permissions
from main.serializers import PostSerializer, ValoracionSerializer
from main.models import Post, Valoracion

class PostViewSet():
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class ValoracionViewSet():
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSerializer
    permission_classes = [permissions.IsAuthenticated]