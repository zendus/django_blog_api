from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Read All Posts': '/all-posts/',
        'Get Post By Id': '/all-posts/<int:pk>',
        'Get Post By Section': '/all-posts/<str:section>',
        'Create New Post': '/create-post/'
    }
    return Response(api_urls)

@api_view(['GET'])
def all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_post_by_id(request, pk):
    post_by_id = Post.objects.get(id=pk)
    serializer = PostSerializer(post_by_id, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_post_by_section(request, section):
    post_by_section = Post.objects.filter(section=section).order_by('pk')
    serializer = PostSerializer(post_by_section, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_new_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Post created successfully')