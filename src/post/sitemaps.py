from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse
from django.utils import timezone

class PostListSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Post.objects.filter(status=1)

    def location(self, item):
        return reverse('frontend:detail_post',args=(item.slug,))

    def lastmod(self, obj):
        return timezone.now()