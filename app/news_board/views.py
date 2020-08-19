from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class VotePostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self, post_id=None):
        if post_id is not None:
            queryset = Post.objects.get(id=post_id)
            return queryset
        else:
            return Post.objects.all()

    def update(self, request, *args, **kwargs):
        if "pk" in self.kwargs:
            post = Post.objects.get(id=self.kwargs.get("pk"))
            post.votes += 1
            post.save()
            serializer = self.get_serializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
