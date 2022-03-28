from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

from .models import Post
from .serializers import PostSerializer

#EN LISTAR TODOS LOS POST QUE EXISTEN 
class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.postobjects.all()[0:4]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

#CLASE PARA VER SOLO UN POST
class PostDetailView(APIView):
    def get(self, resquet, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    