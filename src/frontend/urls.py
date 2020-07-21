from . import views
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from post.sitemaps import PostListSitemap

sitemaps = {
    'posts': PostListSitemap
}



app_name = 'frontend'
urlpatterns = [
    # Sitemaps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',include('robots.urls')),


    path('', views.home,name='home'),
    path('post/<slug:slug>', views.detail_post,name='detail_post'),


]
