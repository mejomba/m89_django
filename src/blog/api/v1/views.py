from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from blog.api.v1.serializers import PostSerializer, PostUpdateSerializer, PostCreateSerializer
from blog.models import Post
from core.models import User


# @authentication_classes([SessionAuthentication, BasicAuthentication])

@api_view()
# @permission_classes([IsAuthenticated])
def post_list(request):
    posts = Post.objects.filter(is_deleted=False)
    se = PostSerializer(posts, many=True)
    return Response(se.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def post_create(request):
    se = PostCreateSerializer(data=request.data)
    user = User.objects.get(id=1)
    if se.is_valid():
        print(se.validated_data)
        print(se.validated_data['category'])
        categoreis = category=se.validated_data['category']
        post = Post.objects.create(title=se.validated_data['title'],
                            content=se.validated_data['content'],
                                   author=user)
        post.save()
        for cat in categoreis:
            for item in cat:
                print(item)
        post.category.add(2, 3)

        post.save()
        new_post = PostSerializer(post)
        return Response(new_post.data)

    return Response({'message': 'data'})


@api_view(["POST"])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    print(request.user)
    # if request.user == post.author:
    #     # post.delete()
    #     post.is_deleted = True
    #     post.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    # else:
    #     return Response({'message': 'your not owner of post'})
    post.is_deleted = True
    post.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def post_update(request, pk):
    try:
        post = Post.objects.get(id=pk)
        # if post.author == request.user:
        #     pass
        se = PostUpdateSerializer(data=request.data)
        if se.is_valid():
            post.title = se.validated_data['title']
            post.content = se.validated_data['content']
            post.save()

            updated_post = PostSerializer(post)
            return Response(updated_post.data)
    except Exception as e:
        print(e)

    return Response({'message': 'pass'})