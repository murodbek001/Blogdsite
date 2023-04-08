from django.urls import path
from .views import *

urlpatterns = [
     path('api/v1/posts/', PostList.as_view(), name="posts_list"),
     path('api/v1/post/<int:pk>/', PostDetail.as_view(), name="nimadir"),
     path('',BlogList.as_view(),name="list"),
     path('api/v1/cats/', CategoryList.as_view(), name="cat_list"),
     path('api/v1/cat/<int:pk>/', CategoryDetail.as_view(), name="nima"),
     path('',CategoryList.as_view(),name="list"),
     path('api/v1/tags/', TagList.as_view(), name="tags_list"),
     path('api/v1/tag/<int:pk>/', TagDetail.as_view(), name="nimaaaa"),
     path('',TagList.as_view(),name="list"),
     path('api/v1/comments/', CommentList.as_view(), name="comments_list"),
     path('api/v1/comment/<int:pk>/', CommentDetail.as_view(), name="nimaaaadd"),
     path('',CommentList.as_view(),name="list"),
     path('cat/<slug:cat_slug>/', CategoryDetail.as_view(), name="cat_detail"),
     path('<slug:slug>/', BlogDetail.as_view(), name="detail"),
]