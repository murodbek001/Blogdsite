from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'image', 'author', 'category', 'tag', 'created', 'updated', )
        read_only_fields = ('id', )
        model = Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',)
        read_only_fields = ('id',)
        model = Category
        #comm tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name',)
        read_only_fields = ('id',)
        model = Tag



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','post','email','text','created')
        read_only_fields = ('id','created')
        model = Comment

