from rest_framework.serializers import Serializer, ModelSerializer

from blog.models import Post, Category


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'content', 'create_at', 'last_update']


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        # fields = ('id', 'name',)
        fields = "__all__"


class PostCreateSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
