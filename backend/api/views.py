from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .serializers import TagSerializer
from rest_framework import permissions

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    #queryset = Post.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination
