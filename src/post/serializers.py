from rest_framework import serializers
from .models import Post,Category
from django.urls import reverse


class PostListSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='author.display_name')
    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), many=True,slug_field='category')
    frontend_slug_url = serializers.SerializerMethodField('create_slug_for_frontend')

    def create_slug_for_frontend(self, foo):
        return reverse('frontend:detail_post',args=(foo.slug,))

    class Meta:
        model = Post
        read_only_fields = ('display_name','title','title_description','category','tags',\
                            'post_thumbnail','created_on','updated_on','slug','frontend_slug_url')
        # exclude = ('id','content')
        fields = ('display_name','title','title_description','category','tags',\
                            'post_thumbnail','created_on','updated_on','slug','frontend_slug_url')




class PostDetailSerializer(serializers.ModelSerializer):
    display_name = serializers.ReadOnlyField(source='author.display_name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), many=True,slug_field='category')
    # list_of_meta_tags = serializers.SerializerMethodField('split_tags')

    # def split_tags(self, foo):
    #     if foo.tags is not None:    
    #         return foo.tags.split(',') 
    #     else:
    #         return []

    class Meta:
        model = Post
        read_only_fields = ('display_name','title','title_description','category','tags',\
                            'content','created_on','updated_on','slug',)
        # exclude = ('id','content')
        fields = ('display_name','title','title_description','category','tags',\
                            'content','created_on','updated_on','slug',)
