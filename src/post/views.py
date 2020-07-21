from django.shortcuts import render
from .models import Post,Category
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import views, mixins, permissions, exceptions, status
from rest_framework.utils import json
from django.utils import timezone
# import requests
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import serializers
from . import paginations

@api_view(['GET'])
def get_all_posts(request):
    paginator = paginations.CursorSetPagination()
    posts = Post.objects.filter(status=1)
    context = paginator.paginate_queryset(posts, request)
    serializer = serializers.PostListSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])
def get_posts_byCategory(request,category):
    paginator = paginations.CursorSetPagination()
    if Post.objects.filter(category__category=category,status=1).exists():
        posts = Post.objects.filter(category__category__contains=category)
        context = paginator.paginate_queryset(posts, request)
        serializer = serializers.PostListSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response({'error':'OOPS! Not found'},status=status.HTTP_404_NOT_FOUND)        


@api_view(['GET'])
def get_all_categories(request):
    all = Category.objects.values_list('category', flat=True)
    return Response({'categories':all})


# @api_view(['GET'])
# def get_detail_post_byID(request,pk):
#     if Post.objects.filter(id=pk,status=1).exists():
#         context = Post.objects.filter(id=pk)[0]
#         serializer = serializers.PostDetailSerializer(context)
#         return Response(serializer.data)
#     return Response({'error':'not found'},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_detail_post_bySlug(request,slug):
    if Post.objects.filter(slug=slug,status=1).exists():
        context = Post.objects.filter(slug=slug)[0]
        serializer = serializers.PostDetailSerializer(context)
        return Response(serializer.data)
    return Response({'error':'OOPS! Not found'},status=status.HTTP_404_NOT_FOUND)


