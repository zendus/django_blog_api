from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Post, Comment
from .serializers import PostSerializer, UserCommentSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Read All Posts': '/all-posts/',
        'Get Post By Id': '/all-posts/<int:pk>',
        'Get Post By Section': '/all-posts/<str:section>',
        'Create New Post': '/create-post/',
        'Update Existing Post By Id': '/update-post/<int:pk>',
        'Delete Existing Post By Id': '/delete-post/<int:pk>',
        'Get comments for each Post using post Id': '/comments/<int:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_by_id(request, pk):
    post_by_id = Post.objects.get(id=pk)
    serializer = PostSerializer(post_by_id, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_by_section(request, section):
    post_by_section = Post.objects.filter(section=section).order_by('pk')
    serializer = PostSerializer(post_by_section, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_new_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Post created successfully')

@api_view(['POST', 'GET'])
@permission_classes([IsAdminUser])
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        return Response(PostSerializer(post).data)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response(f'Post with Id {pk} deleted')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post_comments(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment.all()
    serializer = UserCommentSerializer(comments, many=True)
    return Response(serializer.data)