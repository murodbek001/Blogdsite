from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Post,Comment,Tag
from django.views import View
from django.db.models import Q
from rest_framework import generics
from .models import Post
from .serializers import *


class BlogList(View):
    def get(self,request):
        posts = Post.objects.all()
        search =request.GET.get('search')
        if search:
            posts = Post.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        cats = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, "blog/list.html", {"posts":posts, "cats":cats, "tags":tags})

def post(self,request):
    pass


class BlogDetail(View):
    def get(self,request,slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        return render(request, "blog/detail.html", {"post":post, "comments":comments})


    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, email=email, text = comment, post=post)
        return redirect('detail',slug)
    

class CategoryDetail(View):
    def get(self,request,cat_slug):
        cats = Category.objects.all()
        category = get_object_or_404(Category,slug = cat_slug)
        posts = Post.objects.filter(category=category)
        return render(request, "blog/list.html", {"posts":posts, "cats":cats})
    


def blog_detail(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, "blog/detail.html")


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    lookup_field = 'pk'
    serializer_class = CategorySerializer


class CategoryDetail(View):
    def get(self, request, cat_slug):
        cats = Category.objects.all()
        category = get_object_or_404(Category, slug=cat_slug)
        posts = Post.objects.filter(category=category)
        return render(request, "blog/list.html", {"posts": posts, "cats": cats})
    
    
class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    lookup_field = 'pk'
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    lookup_field = 'pk'
    serializer_class = TagSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    serializer_class = CommentSerializer
