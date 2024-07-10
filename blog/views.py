from rest_framework import viewsets,permissions
from .models import  Blog,Comments
from .serializers import BlogSerializer,CommentsSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        blog=Blog.objects.get(pk=self.request.data['blog_pk'])
        comments=serializer.save()
        blog.comments.add(comments)
        blog.save()



